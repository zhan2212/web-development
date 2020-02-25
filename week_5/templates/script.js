function sendMessage(){
    
    let div = document.getElementById("messages");
    let h = document.createElement("div");
    h.className = "message";
    let t = document.createTextNode(document.getElementById("messageContent").value); 
    h.appendChild(t); 
    div.appendChild(h);

    document.getElementById("messageContent").value = "";

}