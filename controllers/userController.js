const User = require("../models/user")
const path = require("path")

const registerUser = async(req,res) => {
    try{
        const {Firstname, Lastname, email, password, salutation , address, phone, mobile_provider, lang, role} = req.body;
        
        // COMBINE FIRST AND LAST NAME
        const name = `${Firstname} ${Lastname}`;

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
            salutation,
            address,
            phone,
            mobile_provider,
            lang,
            role: role || 'client'
        });

        // SEND RESPONSE
        res.status(201)
        res.sendFile(path.join(__dirname, "../public/userRegistered.html"))
    } catch(error){
        console.error("Registration error:", error);

        res.status(500)
        res.sendFile(path.join(__dirname, "../public/internalError.html"))
    };  
}

module.exports ={
        registerUser
    }
