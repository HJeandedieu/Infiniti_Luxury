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

app.use(express.urlencoded({extended: true}));

app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'public', 'index.html')));

app.post('/submit-student-data', (req, res) => {
    const name = req.body.firstName + " " + req.body.lastName;
    res.send(`Welcome to the portal ${name}`);
})

app.listen(3000, () => console.log('Server running on port 3000'));
