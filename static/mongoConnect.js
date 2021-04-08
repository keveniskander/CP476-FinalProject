const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://admin:1234@projects.rorbz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("sudoku").collection("users");
  // perform actions on the collection object
  client.close();
});