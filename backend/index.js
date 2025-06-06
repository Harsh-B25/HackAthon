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
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, "./public/pdf");
  },
  filename: function (req, file, cb) {
    crypto.randomBytes(12, function (err, bytes) {
        const fn = bytes.toString("hex") + path.extname(file.originalname);    
        cb(null, fn);
    })
  },
});

const upload = multer({ storage: storage });

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

app.post("/gen_sum",upload.single('pdf') ,(req, res) => {
  res.send("Here is your generated summary");
});

app.post("/risk_data", upload.single("pdf"), (req, res) => {
  res.send("Here is your risky data");
});

app.post("/key_terms", upload.single("pdf"), (req, res) => {
  res.send("Here is your key terms");
});

app.listen(PORT, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log(`The server is running on ${PORT}`);
    }
})