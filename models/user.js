const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
    Firstname: {
        type: String,
        required: true,
        trim: true
    },
    Lastname: {
        type:String,
        required: true,
        trim:true,
    },
    email: {
        type: String,
        required: true,
        unique: true,
        lowercase: true,
        trim: true
    },
    password: {
        type: String,
        required: true,
        minlength: 6  
    },
   salutation: {
        type: String,
        required: false,
    },
    address: {
        type:String,
        required: false,
    },
    tele: {
        type: Number,
        required:false,
    },
    mobile_provider: {
        type: String,
        required: false,
    },

    preferredLand: {
        type: String,
        required: false,
    },
    role: {
        type: String,
        enum: ['client', 'retailer'],
        default: 'client'
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("User", userSchema);