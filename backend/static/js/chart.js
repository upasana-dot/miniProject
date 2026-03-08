const labels = salesData.map(item => item.product);
const values = salesData.map(item => item.sales);

if(labels.length > 0){

new Chart(document.getElementById("salesChart"), {
    type: "bar",
    data: {
        labels: labels,
        datasets: [{
            label: "Predicted Sales",
            data: values
        }]
    }
});

}