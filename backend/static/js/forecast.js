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

    if(salesData && salesData.length > 0){

        const barCtx = document.getElementById('barChart');
    
        if(barCtx){
            new Chart(barCtx, {
                type: 'bar',
                data: {
                    labels: months,
                    datasets: [{
                        label: 'Predicted Sales',
                        data: salesData,
                        backgroundColor: '#4CAF50'
                    }]
                }
            });
        }
    
        const lineCtx = document.getElementById('lineChart');
    
        if(lineCtx){
            new Chart(lineCtx, {
                type: 'line',
                data: {
                    labels: months,
                    datasets: [{
                        label: 'Sales Trend',
                        data: salesData,
                        borderColor: '#3F51B5',
                        fill:false
                    }]
                }
            });
        }
    }