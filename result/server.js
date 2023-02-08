const { json } = require('express');
const express = require('express');
const { MongoClient } = require('mongodb');
const mongoose = require('mongoose');

const app = express();
const PORT = 5002;
const HOST = '0.0.0.0';

// Set the view engine
app.set('view engine', 'ejs');

// Connect to the MongoDB database

const uri = "mongodb://root:root@test_mongodb:27017/grades_db?authSource=admin";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });


app.get('/results', async (req, res) => {
  const db = client.db('grades_db');
  const analytics = db.collection('analytics');

  // Retrieve the analytics data from the database
  const data = await analytics.find({}).toArray();

  // Format the data for the HTML table
  const results = data.map(result => {
    return {
      minGrade: result.min_grade,
      maxGrade: result.max_grade,
      averageGrade: result.avg_grade
    };
  });

  // Send the results as JSON
  res.render('./template.ejs', { results });
});

// Start the Express server
app.listen(PORT, HOST, () => {
  console.log('Running on http://${HOST}:${PORT}');
});