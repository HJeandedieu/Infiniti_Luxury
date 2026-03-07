const User = require("../models/user")

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
        res.status(201).json({
            success:true,
            message: 'User registered successfully',
            data: {
                _id: user._id,
                Firstname: user.Firstname,
                Lastname: user.Lastname,
                email: user.email,
                role: user.role
            }
        });
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
