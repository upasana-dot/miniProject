const container = document.getElementById("container");
const params = new URLSearchParams(window.location.search);
const mode = params.get("mode");

if(mode === "login"){
    document.getElementById("container").classList.remove("active");
} else if(mode === "register"){
    document.getElementById("container").classList.add("active");
}

document.getElementById("goRegister").onclick = () => {
    document.getElementById("container").classList.add("active");
};

document.getElementById("goLogin").onclick = () => {
    document.getElementById("container").classList.remove("active");
};
function toggleTheme(){
    document.body.classList.toggle("dark");
}