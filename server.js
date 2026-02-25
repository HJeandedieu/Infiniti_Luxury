const express = require("express")
const path = require("path")
const routes = require("./routes/pageRoutes.js");
const middleware = require("./middleware/middleware.js")
const connectDB = require("./db/db.js")

const app = express()
const PORT = 3000;

//Connect to MongoDB
connectDB();

app.use(express.static(path.join(__dirname, "public")));
app.use(middleware)

app.use("/", routes)
app.use((req,res)=>{
    res.status(404).sendFile(path.join(__dirname, "/public/404.html"));
})

app.listen(PORT, ()=>{
    console.log("Server is running on Port " + PORT)
})