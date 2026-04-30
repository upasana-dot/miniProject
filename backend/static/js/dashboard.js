fetch("/forecast")

.then(res => res.json())

.then(data => {

document.getElementById("forecast").innerText =
"Predicted Sales: " + data.prediction

})
