const express = require("express")
const path = require("path")
const app = express()
const routes = require("./routes/pageRoutes.js")
const PORT = 3000;

app.use(express.static(path.join(__dirname, "public")));

app.use("/", routes)
app.use((req,res)=>{
    res.status(404).sendFile(path.join(__dirname, "/public/404.html"));
})

app.listen(PORT, ()=>{
    console.log("Server is running on Port " + PORT)
})