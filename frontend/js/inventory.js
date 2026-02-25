console.log("Inventory Page Loaded");

// Example reorder logic
const inventory = [
    { product: "Product A", stock: 120, reorder: 150 },
    { product: "Product B", stock: 300, reorder: 200 }
];

inventory.forEach(item => {
    if (item.stock < item.reorder) {
        console.log(item.product + " needs reorder");
    }
});
