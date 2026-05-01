//Ares Application - Frontend
//exress app that serves ejs files
var express = require('express');
var app = express();
app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL;

const fetch = (...args) =>
  import('node-fetch').then(({ default: fetch }) => fetch(...args));

app.get('/', (req, res) => {
  res.render('index', { submittedData: null });
});

app.post('/submit', async function(req, res) {  
  console.log("FORM DATA:", req.body);
  try {
    const response = await fetch(process.env.BACKEND_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(req.body)
    });

    const data = await response.json();

    res.render('index', { submittedData: req.body });
  } catch (err) {
    console.log(err);
    res.status(500).send("Error submitting form");
  }
});

app.get('/', function(req, res) {
  res.render('index');
});

app.listen(3000, function() {
  console.log('Frontend app listening on port 3000!');
});