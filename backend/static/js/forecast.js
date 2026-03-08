function getForecast(){

    let product = document.getElementById("product").value
    
    fetch("/api/product_forecast/" + product)
    
    .then(res => res.json())
    
    .then(data => {
    
    document.getElementById("prediction").innerText =
    "Predicted Sales: " + data.predicted_sales
    document.getElementById("barChart")
    document.getElementById("lineChart")
    
    })
    
    }