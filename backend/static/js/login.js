const container = document.getElementById("container");

document.getElementById("goRegister").onclick = () => {
    container.classList.add("active");
};

document.getElementById("goLogin").onclick = () => {
    container.classList.remove("active");
};
function toggleTheme(){
    document.body.classList.toggle("dark");
}