const User = require("../models/user")
const path = require('path')

const registerUser = async(req,res) => {
    try{
        const {name, email, password} = req.body;

        // SIMPLE VALIDATION
        if(!name || !email || !password){
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
            name,
            email,
            password,
            address,
            tele,
            mobile_provider,
            preferredLand
        });

        // SEND RESPONSE
        // res.status(201).json({
        //     success:true,
        //     message: 'User registered successfully',
        //     data: {
        //         _id: user._id,
        //         name: user.name,
        //         email: user.email
        //     }
        // });

        // SEND A RESPONSE
        res.status(201).sendFile(path.join(__dirname, "../public/userRegistered.html"));
    } catch(error){
        console.error("Registration error:", error);

        res.status(500).json({
            success: false,
            message: "Internal Server Error"
        });
    };  
}

module.exports ={
        registerUser
    }
