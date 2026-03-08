
fetch("/api/inventory")

.then(response => response.json())

.then(data => {

let table = document.getElementById("inventoryTable");

data.forEach(item => {

let row = `<tr>

<td>${item.product}</td>
<td>${item.stock}</td>
<td class="${item.stock < 20 ? 'low':'ok'}">
${item.stock < 20 ? 'Reorder Needed':'In Stock'}
</td>

</tr>`;

table.innerHTML += row;

});

});