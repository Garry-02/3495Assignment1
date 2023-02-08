const express = require('express');
const { MongoClient } = require('mongodb');
const mongoose = require('mongoose');

const app = express();

const PORT = 5002;
const HOST = '0.0.0.0';


// Connect to the MongoDB database

const uri = "mongodb://root:root@test_mongodb:27017/grades_db?authSource=admin";

const studentResultSchema = new mongoose.Schema({
  minGrade: Number,
  maxGrade: Number,
  averageGrade: Number
});

const StudentResult = mongoose.model('StudentResult', studentResultSchema);

app.get("/analytics", async (req, res) => {
  const client = new MongoClient(uri, { useNewUrlParser: true });

  try {
    await client.connect();

    const db = client.db("grades_db");
    const analytics = db.collection("analytics");
    const analyticsData = await analytics.find().toArray();

    res.send(analyticsData);
  } catch (error) {
    console.error(error);
    res.status(500).send(error);
  } finally {
    client.close();
  }
});

// Route to get the results
/* app.get('/results', (req, res) => {
  StudentResult.find({}, (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    return res.send(results);
  });
}); */

// Start the Express server
app.listen(PORT, HOST, () => {
  console.log('Running on http://${HOST}:${PORT}');
});