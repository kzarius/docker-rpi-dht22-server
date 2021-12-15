'use strict';

const express = require('express');
const fs = require('fs');

const app = express();
app.get('/',(req,res)=>{

    // We're using a file to save the readings, so we don't need to wait
    // on the sensor query, which could take awhile.
    fs.readFile('./db/readings.txt','utf8',(err,data)=>{
        if(err){
            // Remember to check against 'error' first when handling the JSON return.
            res.send('{"error":"true"}');
        }else{
            // Will return a JSON object: {timestamp, temp, humidity}
            res.send(data);
        }
    })

});

// If you need to listen on a different port, change the outward facing port in docker-compose.yml
app.listen(4000,()=>console.log('Application listening on port 4000'))