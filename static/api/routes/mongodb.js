var express = require("express");
var router = express.Router();



router.get("/users", function(req, res, next) {

    var MongoClient = require('mongodb').MongoClient;

    var url = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
    MongoClient.connect(url, function(err, db) {

    if (err) throw err;
    var dbo = db.db("sudoku");
    // var myobj = { name: "test", address: "time" };

    dbo.collection('users').find({}).sort({_id:-1}).limit(5).toArray(function(err,result){
        if (err) throw err;
        
        console.log(result)
        res.send(JSON.stringify(result));
        
        db.close();
        

    });
    


    console.log('test1');
    

    

});

});

router.get("/insertusers/:name/:time", function(req, res, next) {
    var MongoClient = require('mongodb').MongoClient;

    var url = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
 

    MongoClient.connect(url, function(err, db) {
        
        
        
        if (err) throw err;
        var dbo = db.db("sudoku");
        var myobj = { name: req.params.name, address: req.params.time};
        dbo.collection("users").insertOne(myobj, function(err, res) {

            if (err) throw err;
            console.log("1 document inserted into chat database");

            
            
            db.close();
        });
        // console.log(inserted)
      

        
    });

    res.send("inserted");


    

});
module.exports = router;