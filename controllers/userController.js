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
