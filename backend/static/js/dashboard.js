// const ctx = document.getElementById('inventoryChart');

// new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['Jan','Feb','Mar','Apr','May','Jun'],
//         datasets: [{
//             label: 'Inventory Usage',
//             data: [50,60,55,70,90,120],
//             borderWidth: 2
//         }]
//     }
// });

fetch("/forecast")

.then(res => res.json())

.then(data => {

document.getElementById("forecast").innerText =
"Predicted Sales: " + data.prediction

})