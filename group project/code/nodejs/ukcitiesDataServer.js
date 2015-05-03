#!/usr/bin/env node

// API Funtions for uk cities project
//author paula

var moment = require('E:/data/paula/geospatial/ukcities/node_modules/moment');

var portNumber = 3000;

var mysql = require('E:/data/paula/geospatial/ukcities/node_modules/mysql');

// MySQL Connection Variables
var connection = mysql.createConnection({
  host     : '128.40.150.34',
  user     : 'ucfnpwh',
  password : 'kufefopuno',
  database : 'ucfnpwh'
});

connection.connect();

//  Setup the Express Server
var express = require('E:/data/paula/geospatial/ukcities/node_modules/express')
var app = express()
app.set('view engine', 'ejs');

// Provides the static folders we have added in the project to the web server.
app.use(express.static(__dirname + '/js'));
app.use(express.static(__dirname + '/css'));
app.use(express.static(__dirname + '/images'));


//new function
app.get('/data/cities', function (req, res) {
      // Allows data to be downloaded from the server with security concerns
      res.header("Access-Control-Allow-Origin", "*");
      res.header("Access-Control-Allow-Headers", "X-Requested-WithD");

      // SQL Statement to run
      var sql = "SELECT name, lat,lon from City";

      // Log it on the screen for debugging
      console.log(sql);

      // Run the SQL Query
      connection.query(sql, function(err, rows, fields) {
              if (err) console.log("Err:" + err);
              if(rows != undefined){
                      // If we have data that comes bag send it to the user.
                      res.send(rows);
              }else{
                      res.send("");
              }
      });
});


// Setup the server and print a string to the screen when server is ready
var server = app.listen(portNumber, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('App listening at http://%s:%s', host, port);
})

