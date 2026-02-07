import express from "express";
import QRCode from "qrcode";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";  // <-- import this

// Fix __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());
app.use(express.static(path.join(__dirname, "public"))); // works now

// Ensure QR folder exists
const qrFolder = path.join(__dirname, "public", "qrcodes");
if (!fs.existsSync(qrFolder)) fs.mkdirSync(qrFolder, { recursive: true });

app.post("/api/qrcodes", async (req, res) => {
    const { data } = req.body;
    if (!data) return res.status(400).json({ error: "Data is required" });

    const filename = `qr_${Date.now()}.png`;
    const filepath = path.join(qrFolder, filename);

    try {
        await QRCode.toFile(filepath, data);
        res.status(201).json({ message: "QR code generated", url: `/qrcodes/${filename}` });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "QR generation failed" });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
