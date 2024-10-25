// Import express
const express = require('express');

// Initialize the app
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Welcome');
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
