import crypto from "crypto"
import express from "express"
import fs from "fs";
const app = express();

app.set("view engine", "ejs")
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

import {fileURLToPath} from "url";
import path from "path"
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
app.use(express.static(path.join(__dirname, "public")));

import dotenv from "dotenv";
dotenv.config();
const PORT = process.env.PORT;

import multer from "multer"

import session from "express-session";
app.use(
  session({
    secret: "keyboard cat",
    resave: false,
    saveUninitialized: true,
  })
);

let ofn;
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "./public/pdf");
  },
    filename: function (req, file, cb) {
        ofn = file.originalname;
    crypto.randomBytes(12, function (err, bytes) {
        const fn = bytes.toString("hex") + path.extname(file.originalname);   
        // console.log(fn);
        req.session.uniqueName = fn;
        // console.log(req.uniqueName);
        cb(null, fn);
    })
  },
});

const upload = await multer({ storage: storage });
import { spawn } from "child_process";


const generate_summ = (filename) => {
    return new Promise((resolve, reject) => {
        console.log("Data is being sent to the Python file...");
        console.log(filename);
        const filePath = path.join(__dirname, `./public/pdf/${filename}`);
        const python = spawn("python", [
          "../summarise.py",
          filePath,
        ]);

        let dataString = "";

        python.stdout.on("data", (data) => {
            dataString += data.toString();
        });

        python.stderr.on("data", (err) => {
            console.error("Python error:", err.toString());
        });

        python.on("close", (code) => {
            console.log("Python process exited with code", code);
            resolve(dataString); // return final output here
        });

        python.on("error", (err) => {
            reject(err);
        });
    });
};

const generate_risks = (filename) => {
  return new Promise((resolve, reject) => {
    console.log("Data is being sent to the Python file...");
    console.log(filename);
    const filePath = path.join(__dirname, `./public/pdf/${filename}`);
    const python = spawn("python", [
      "../taking_out_mistakes.py",
      filePath,
    ]);

    let dataString = "";

    python.stdout.on("data", (data) => {
      dataString += data.toString();
    });

    python.stderr.on("data", (err) => {
      console.error("Python error:", err.toString());
    });

    python.on("close", (code) => {
      console.log("Python process exited with code", code);
      resolve(dataString); // return final output here
    });

    python.on("error", (err) => {
      reject(err);
    });
  });
};

const extract_flowchart = (filename) => {
  return new Promise((resolve, reject) => {
    console.log("Data is being sent to the Python file...");
    console.log(filename);
    const filePath = path.join(__dirname, `./public/pdf/${filename}`);
    const python = spawn("python", [
      "../extract_key_terms.py",
      filePath,
    ]);

    let dataString = "";

    python.stdout.on("data", (data) => {
      dataString += data.toString();
    });

    python.stderr.on("data", (err) => {
      console.error("Python error:", err.toString());
    });

    python.on("close", (code) => {
      console.log("Python process exited with code", code);
      resolve(dataString); // return final output here
    });

    python.on("error", (err) => {
      reject(err);
    });
  });
};

const generate_pdf = (
  agreement_date,
  company_name,
  company_jurisdiction,
  company_address,
  consultant_name,
  consultant_jurisdiction,
  consultant_address,
  purpose_description,
  confidentiality_term_years,
  governing_law,
  company_signatory_name,
  company_signatory_title,
  consultant_signatory_name,
  consultant_signatory_title,
  type,
  res
) => {
  return new Promise((resolve, reject) => {
    console.log("Data is being sent to the Python file...");
    const scriptPath = `/Users/aryangoyal/Desktop/cyfuture_hackthon/cloning work/HackAthon/${type}.py`;
    const outputPath = `/Users/aryangoyal/Desktop/cyfuture_hackthon/backend/confidentiality.pdf`;
    const python = spawn("python", [
      `../cloning work/HackAthon/${type}`,
      agreement_date,
      company_name,
      company_jurisdiction,
      company_address,
      consultant_name,
      consultant_jurisdiction,
      consultant_address,
      purpose_description,
      confidentiality_term_years,
      governing_law,
      company_signatory_name,
      company_signatory_title,
      consultant_signatory_name,
      consultant_signatory_title,
    ]);

    python.stderr.on("data", (err) => {
      console.error("Python error:", err.toString());
    });
  
    python.on("close", (code) => {
      console.log("Python process exited with code", code);
      if (code === 0) {
        // Wait 500ms to ensure the PDF file is written to disk
        setTimeout(() => {
          if (fs.existsSync(outputPath)) {
            resolve(outputPath);
          } else {
            reject(
              new Error(`PDF not found even though process exited with code 0`)
            );
          }
        }, 500);
      } else {
        reject(new Error(`PDF generation failed (exit code ${code})`));
      }
    });
  
    python.on("error", (err) => {
      console.error("Failed to start Python script:", err);
      res.status(500).send("Internal Server Error");
    });
  });
};


app.get("/", (req, res) => {
    try {      
        res.render("index.ejs");
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "Some error in finding the home page",
        });
    }
})
app.post("/analyze_document", upload.single('pdf'), (req, res) => {
    console.log("This data has reached successfully");
    res.redirect("/1st_feature");
});
let data;
let data2;
let data3;
app.get("/1st_feature", async (req, res) => {
    try {
        console.log(req.session.uniqueName);
        await generate_summ(req.session.uniqueName).then(summary => {
            data = summary;
        }).catch(err => {
            console.error("Error:", err);
        })
        await generate_risks(req.session.uniqueName)
          .then((summary) => {
            data2 = summary;
          })
          .catch((err) => {
            console.error("Error:", err);
          });
          await extract_flowchart(req.session.uniqueName)
            .then((summary) => {
              data3 = summary;
            })
            .catch((err) => {
              console.error("Error:", err);
            });
        res.render("1st_feature.ejs", { data,ofn,data2,data3 });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "The file has not been chosen yet",
        })
    }
})

app.post("/generate_contract", (req, res) => {
  res.render("3rd_feature.ejs");
})

app.post("/retrieving_data", async (req, res) => {
  try {
    const pdfPath = await generate_pdf(
      req.body.agreement_date,
      req.body.company_name,
      req.body.company_jurisdiction,
      req.body.company_address,
      req.body.consultant_name,
      req.body.consultant_jurisdiction,
      req.body.consultant_address,
      req.body.purpose_description,
      req.body.confidentiality_term_years,
      req.body.governing_law,
      req.body.company_signatory_name,
      req.body.company_signatory_title,
      req.body.consultant_signatory_name,
      req.body.consultant_signatory_title,
      req.body.template
    );

    if (fs.existsSync(pdfPath)) {
      res.setHeader("Content-Type", "application/pdf");
      res.setHeader("Content-Disposition", "inline");
      fs.createReadStream(pdfPath).pipe(res);
    } else {
      res.status(404).send("PDF not found");
    }
  } catch (err) {
    console.error("Error generating PDF:", err);
    res.status(500).send("Internal Server Error");
  }

});
app.listen(PORT, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log(`The server is running on ${PORT}`);
    }
})