import crypto from "crypto"
import express from "express"
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
          "/Users/aryangoyal/Desktop/cyfuture_hackthon/summarise.py",
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
      "/Users/aryangoyal/Desktop/cyfuture_hackthon/taking_out_mistakes.py",
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
        res.render("1st_feature.ejs", { data,ofn,data2 });
    } catch (err) {
        res.status(500).json({
            success: false,
            message: "The file has not been chosen yet",
        })
    }
})

app.listen(PORT, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log(`The server is running on ${PORT}`);
    }
})