console.log("Forecast Page Loaded");

// Example forecast logic
const forecastData = [
    { product: "Product A", demand: 150 },
    { product: "Product B", demand: 220 }
];

forecastData.forEach(item => {
    console.log(item.product + " → " + item.demand);
});
fetch("http://127.0.0.1:5000/api/forecast")
.then(res => res.json())
.then(data => {
    console.log(data.next_month_prediction);
});
