const fs = require("fs")
const path = require("path")

function trackVisits(req,res,next){
    console.log("Visit logged successfully!")
    next();
}

module.exports = trackVisits;