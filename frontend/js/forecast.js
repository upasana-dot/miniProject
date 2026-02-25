console.log("Forecast Page Loaded");

// Example forecast logic
const forecastData = [
    { product: "Product A", demand: 150 },
    { product: "Product B", demand: 220 }
];

forecastData.forEach(item => {
    console.log(item.product + " → " + item.demand);
});
