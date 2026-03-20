let isSignup = false;

function switchToSignup(){
    const title = document.getElementById("formTitle");
    const form = document.getElementById("authForm");

    if(!isSignup){
        title.innerText = "Sign Up";

        form.innerHTML = `
            <div class="input-box">
                <input type="text" placeholder="Username" required>
            </div>

            <div class="input-box">
                <input type="email" placeholder="Email" required>
            </div>

            <div class="input-box">
                <input type="password" placeholder="Password" required>
            </div>

            <button type="submit" class="btn">Sign Up</button>
        `;

        isSignup = true;
    }
}