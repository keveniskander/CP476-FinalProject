var express = require("express");
var router = express.Router();

router.get("/", function(req, res, next) {

    var MongoClient = require('mongodb').MongoClient;

    var url = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("sudoku");
    var myobj = { name: "test", address: "time" };
    dbo.collection("users").insertOne(myobj, function(err, res) {
        if (err) throw err;
        console.log("1 document inserted");
        db.close();
    });
    });
    console.log('test1');
    res.send("API is working properly");

});

module.exports = router;