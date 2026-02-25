const fs = require("fs")
const path = require("path")

const logFile = path.join(__dirname, "visits.json");


function trackVisits(req,res,next){
    const visit = {
        path:req.originalUrl,
        method: req.method,
        timestamp: new Date().toISOString(),
        ip:req.ip,
    };

    fs.appendFile(logFile, JSON.stringify(visit) + '\n', (err)=>{
        if(err){
            console.error("Couldn't log visit info");
            console.error(err.message);
        }

        console.log("Visit logged successfully!")
    })
    next();
}

module.exports = trackVisits;