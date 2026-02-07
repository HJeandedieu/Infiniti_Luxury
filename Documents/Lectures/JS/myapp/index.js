// const express = require('express');
// const app = express();
// const port = 3000;

// app.get('/',(req,res) =>{
//     res.send("Hello World!")
// })


// app.get('/about',(req,res) => {
//     res.send('About Us Page');
// })

// app.listen(port, ()=>{
//     console.log(`Example app listening on port ${port}`)
// })


// app.use((req, res, next) => {
//     console.log(req.method, req.url);
//     next();
// })


// const express = require('express');
// const app = express();

// app.use((req, res, next) => {
//     console.log('Middleware 1: logger');
//     console.log(req.method, req.url);
//     if(req.url === '/students'){
//         res.send('Students Page')
//     }
//     next();
// })

// app.use((req, res, next) => {
//     console.log('Middleware 2: Authentiation');

//     if(req.url === '/blocked'){
//         return res.send('Access Denied')
//     }

//     next();
// })


// app.get('/', (req,res) => {
//     console.log('Route Handler: Home');
//     res.send('Hello from Home Page');

    
// })


// app.listen(3000, () => {
//     console.log('Server running on port 3000')
// });


//ROUTING IN EXPRESS

// const express = require('express');
// const app = express();

// app.get('/users', (req, res) => {
//     res.send('List of users');
// })


// app.get('/users', (req, res) => {
//     res.send('Create a new user')
// });

// app.get('/users/:id', (req, res) => {
//     const userId = req.params.id;
//     res.send(`User with ID: ${userId}`);
// });


// app.listen(3000, () => {
//     console.log('Server is running on port 3000')
// })


// const express = require('express');
// const router = express.Router();


// router.get('/', (req, res) => res.send("Home Page"));
// router.get('/about', (req, res) => res.send('About Page'));
// router.get('/contact', (req, res) => res.send('Contact Page'));
// router.get('/blocked', (req, res) => res.send('Acess Denied'))
// router.get('/unvailable', (req, res) => res.status(404).send('statusCode: 404\nNot Found'))


// module.exports = router;

// const express = require('express');
// const app = express();

// const path = require('path');

// const filePath = path.join(__dirname, 'public')

// app.use(express.static(filePath));

// app.listen(3000,'0.0.0.0', () => {
//     console.log('Server running on port 3000')
// })

// app.get('/about', (req, res) => {
//     res.send('About us Page')
// })


const express = require('express');
const app = express();
const path = require('path');


//Middleware to parse JSON bodies
app.use(express.json());


//Serve frontend static files
app.use(express.static(path.join(__dirname, 'public')));


// Mount API routes under /api

const apiRoutes = require('./routes/api.js');
app.use('/api', apiRoutes);


//Fallback route for SPA or frontend routing

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(3000, () => {
    console.log('Server running on port 3000')
})