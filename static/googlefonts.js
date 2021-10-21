function getGoogleFonts(){
    fetch('https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyBdiCkRQ2XjA2ufp6DGnB0SNJSPEiTgDQI')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
}
function sample(){
    console.log("working!")
}