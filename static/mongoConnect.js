// var mongo = require('mongodb');

// const MongoClient = require('mongodb').MongoClient;
// const uri = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
// client.connect(err => {
//   const collection = client.db("sudoku").collection("users");
//   // perform actions on the collection object
//   client.close();
// });


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

function test(){
  console.log('button test')
}