'use strict';

const express = require('express');
const fs = require('fs');

// App
const app = express();
app.get('/',(req,res)=>{

    fs.readFile('./readings.txt','utf8',(err,data)=>{
        if(err){
            res.send('{"error":"true"}');
        }else{
            res.send(data);
        }
    })

});

app.listen(80,()=>console.log('Application listening on port 80'))