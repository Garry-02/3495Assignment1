const express = require('express');
const mongoose = require('mongoose');

const app = express();

const PORT = 5002;
const HOST = '0.0.0.0';


// Connect to the MongoDB database
mongoose.connect('mongodb://mongodb:27017/student_results', { useNewUrlParser: true });

const studentResultSchema = new mongoose.Schema({
  minGrade: Number,
  maxGrade: Number,
  averageGrade: Number
});

const StudentResult = mongoose.model('StudentResult', studentResultSchema);

// Route to get the results
app.get('/api/results', (req, res) => {
  StudentResult.find({}, (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    return res.send(results);
  });
});

// Start the Express server
app.listen(PORT, HOST, () => {
  console.log('Running on http://${HOST}:${PORT}');
});