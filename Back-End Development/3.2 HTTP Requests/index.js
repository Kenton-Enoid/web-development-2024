import express from "express";

const app = express();
const port = 3000;

app.get("/", (req, res) => {
    res.send("<h1>Hello Ninja!</h1>");
})

app.get("/about", (req, res) => {
    res.send("<p>I just love coding man and building fun stuff!</p>");
})
app.get("/contact", (req, res) => {
    res.send("<h3>Hit me up here: 06387643866</h3>")
})
app.listen(port, () => {
    console.log(`Server running on port ${port}.`);
})