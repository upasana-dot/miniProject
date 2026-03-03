// function login() {
//     // Dummy login (can connect backend later)
//     alert("Login Successful");
//     window.location.href = "dashboard.html";
// }

function login() {
    const username = document.querySelector("input[type='text']").value;
    const password = document.querySelector("input[type='password']").value;

    fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        if(data.message === "Login successful"){
            window.location.href = "dashboard.html";
        }
    });
}
