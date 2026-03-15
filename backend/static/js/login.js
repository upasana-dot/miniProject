document.getElementById("loginForm").addEventListener("submit",function(e){
    document.getElementById("btnText").style.display="none";
    document.getElementById("spinner").style.display="block";
    
    document.getElementById("loginForm").addEventListener("submit", function(){
    document.getElementById("spinner").style.display="block";    
    });    
    window.location.href="/home"
    
    })