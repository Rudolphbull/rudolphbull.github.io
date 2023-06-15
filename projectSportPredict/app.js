
const express = require("express");

const bodyParser = require("body-parser");

const request = require("request");

const https = require('https');
// const { log } = require("console");

const app = express();

app.use(express.static("public"));

app.use(bodyParser.urlencoded({extended: true}));

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index2.html");
});

app.get("/MoneyDoublersOnly", function(req, res){
    res.sendFile(__dirname + "/todaysbookings.html");
});

app.get("/Signup", function(req, res){
    res.sendFile(__dirname + "/signup.html");
});

app.get("/success", (req, res)=>{
    res.render("success");
});

app.get("/failure", (req, res)=>{
    res.render("failure");
});

app.post("/", function(req, res){
    const firstname = req.body.fName;
    const lastname = req.body.lName;
    const email = req.body.email;

    const data = {
        members: [
            {
                email_address: email,
                status: "subscribed",
                merge_fields: {
                    FNAME: firstname,
                    LNAME: lastname
                }
            }
        ]
    };

    const jsonData = JSON.stringify(data);

    const url = "https://us21.api.mailchimp.com/3.0/lists/98f9b98053";

    const options = {
        method: "POST",
        auth: "Rudolphbull:85e4672c906b9c22717550c720197125-us21"
    }
    const request = https.request(url, options, function(response){

        if (response.statusCode === 200){
            res.sendFile(__dirname + "/success.html");
        } else{
            res.sendFile(__dirname + "/f.html");
        }
        response.on("data", function(data){
            console.log(JSON.parse(data));
        })

    });

    request.write(jsonData);
    request.end();

    // console.log(firstname, lastname, email);
});

//date and time
let nowVar = new Date();

let time = document.getElementById("now");

time.innerHTML = nowVar;

app.listen(3000, function(req, res){
    console.log("Server is running on port 3000.");
});

//api key Mailchimp: 85e4672c906b9c22717550c720197125-us21
// audience id: 98f9b98053