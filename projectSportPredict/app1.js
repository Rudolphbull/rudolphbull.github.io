const express = require("express");

const bodyParser = require("body-parser");

const mongoose = require("mongoose");

const ejs = require("ejs");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({extended: true}));

app.use(express.static("public"));

// app.use(express.urlencoded({extended: false}));

// Connect DB

mongoose.connect("mongodb://localhost:27017/profpredictDB", {useNewUrlParser: true, useUnifiedTopology: true}).then((err)=>{
    console.log("DB connected successfully to profpredictDB...");
    app.listen(4000, ()=>{
        console.log("Application Server started on port 4000...");
    });
}).catch(()=>{
    console.log("failed to connect to profpredictDB!!!" + err);
});

// create Schema

const profpredictSchema = new mongoose.Schema({
    username: {
        type: String,
        required: [true, "username is required"]
    },
    email: {
        type: String,
        require: [true, "email is required"],
        unique: true
    },
    password: {
        type: String,
        required: [true, "password is required"]
    },
    confirmPassword: {
        type: String,
        required: [true, "confirm password is required"]
    },
},
{
    timestamps: true
});


// create Model

const profpredictModel = mongoose.model("staker", profpredictSchema);

// add data to database

// const Rudolphbull = new profpredictModel({
//     username: "rudolphbull",
//     email: "rudolphbull@gmail.com",
//     password: "Welcome123@",
//     confirmPassword: "Welcome123@"
// });

// const GMA = new profpredictModel({
//     username: "gma",
//     email: "gma@gmail.com",
//     password: "Welcome432@",
//     confirmPassword: "Welcome432@"
// });

// const Prof = new profpredictModel({
//     username: "prof",
//     email: "prof@gmail.com",
//     password: "Welcome321@",
//     confirmPassword: "Welcome321@"
// });

// const defaultNames = [Rudolphbull, GMA, Prof];
// profpredictModel.insertMany(defaultNames).then((stakers, err)=>{
//     console.log("Stakers information added to the database...");
//     console.log(stakers);
// }).catch(()=>{
//     console.log("Failed to add stakers information to the database!!" + err.message);
// });

// Routes

app.get("/", (req, res)=>{
    res.render("home");
});

app.get("/MoneyDoublersOnly", (req, res)=>{
    res.render("login");
});

app.get("/predictions", (req, res)=>{
    res.render("predictions");
});


app.get("/login", (req, res)=>{
    res.render("login");
});

app.get("/Signup", (req, res)=>{
    res.render("signup");
});

app.get("/Career", (req, res)=>{
    res.render("career");
});

app.get("/About", (req, res)=>{
    res.render("about");
});

app.get("/Contact", (req, res)=>{
    res.render("contact");
});

app.get("/success", (req, res)=>{
    res.render("success");
});

app.get("/failure", (req, res)=>{
    res.render("failure");
});

app.post("/signup", async(req, res)=>{

    const data = {
        username: req.body.username,
        email: req.body.email,
        password: req.body.password,
        confirmPassword: req.body.confirmPassword
    }

    await profpredictModel.insertMany([data]).then((stakers, err)=>{

            if (stakers) {
                res.redirect("success");
            } else{
                res.redirect("failure");
            }
        }).catch(()=>{
            res.send("Failed to add stakers information to the database!!" + err.message);
        });

    // res.render("todaysbookings"); am suspecting this has no business here...
});

app.post("/login", async(req, res)=>{

    try {    
        const checkUsername = await profpredictModel.findOne({username: req.body.username});
        const checkUseremail = await profpredictModel.findOne({email: req.body.email});

        if (checkUsername.password === req.body.password) {
            res.render("todaysbookings");
        }
       
        else if (checkUseremail.password === req.body.password) {
            res.render("todaysbookings");
        } 

        else{
            res.send("Wrong Password...");
        }
    
}
    catch (error) {
        res.send("Wrong details!!!");
        
    }

});


