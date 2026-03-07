const User = require("../models/user")
const path = require('path')

const registerUser = async(req,res) => {
    try{
        const {Firstname, Lastname, email, password, address, tele, mobile_provider, preferredLand} = req.body;

        // SIMPLE VALIDATION
        if(!Firstname || !Lastname || !email || !password){
            return res.status(400).json({
                success:false,
                message:"All fields are required"
            });
        }

        // CHECK IF USER EXISTS
        const userExists = await User.findOne({email});

        if (userExists){
            return res.status(400).json({
                success: false,
                message:"User already Exists"
            });
        }

        // CREATE USER
        const user =  await User.create({
            Firstname,
            Lastname,
            email,
            password,
            address,
            phone,
            mobile_provider,
            lang
        });
        
        // SEND A RESPONSE
        res.status(201).sendFile(path.join(__dirname, "../public/userRegistered.html"));
    } catch(error){
        console.error("Registration error:", error);

        res.sendFile(path.join(__dirname, "../public/internalError.html"))
    };  
}

module.exports ={
        registerUser
    }
