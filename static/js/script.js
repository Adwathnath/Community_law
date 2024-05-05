

// Example POST method implementation
async function postData(url = "", data= {}) {
    // Default option are marked with *
    const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json", // 'Content-Type': 'application/x-www-form-urlencoded', 
        },
       body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}


sendButton.addEventListener("click", async ()=>{
    
    questionInput = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questionInput;
    question2.innerHTML = questionInput;

    //Get the answer and populate it
    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML = result.answer
    document.querySelector(".box2").scrollTop = document.querySelector(".box2").scrollHeight

})

sendButton2.addEventListener("click", async ()=>{
    
    questionInput2 = document.getElementById("questionInput2").value;
    document.getElementById("questionInput2").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    question1.innerHTML = questionInput2;
    question2.innerHTML = questionInput2;

    //Get the answer and populate it
    let result = await postData("/api", {"question": questionInput2})
    solution.innerHTML = result.answer
    document.querySelector(".box2").scrollTop = document.querySelector(".box2").scrollHeight

})