const express = require("express");
const path = require("path");

const router = express.Router()

router.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname, "../public/index.html"))
})

router.get("/retailer", (req,res)=>{
    res.sendFile(path.join(__dirname, "../public/retailer.html"))
})

router.get("/build",(req,res)=>{
    res.sendFile(path.join(__dirname, "../public/build.html"))
})

router.get("/search-inventory",(req,res)=>{
    res.sendFile(path.join(__dirname, "../public/search-inventory.html"))
})

router.get("/offers", (req,res)=>{
    res.sendFile(path.join(__dirname, "../public/offers.html"))
})

module.exports = router;