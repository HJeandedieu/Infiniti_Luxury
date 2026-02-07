const express = require('express');
const router = express.Router();

//GET /api/useers

router.get('/users', (req, res) => {
    const users = [
        {id:1, name:'Alice'},
        {id:2, name:'Bob'},
    ];
    res.json(users);
})

//POST /api/users

router.post('/users', (req, res) => {
    res.json({message: 'User created successfully'});
});


module.exports = router;