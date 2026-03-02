const mongoose = require("mongoose")

const uri = 'mongodb://127.0.0.1:27017/infiniti';

async function connectDB(){
    try{
        await mongoose.connect(uri);
        console.log("Connected to MongoDB");
    }catch (err){
        console.error("MongoDB connection error:", err);
        process.exit(1)
    }
}

module.exports = connectDB;