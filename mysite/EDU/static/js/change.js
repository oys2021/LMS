let update=document.getElementsByClassName('update');
for(i=0;i<update.length;i++){
update[i].addEventListener('click',function(){
    let productId = this.dataset.product
    // research on the this.something no
    let action=this.dataset.action

    


    if (user === "AnonymousUser"){
        alert("User is not logged in");
    }
    else{
        updateCart(productId, action)
    }
    
    


})








}
function updateCart(id, action){
    let url = "/update"
    fetch(url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": id, "action": action})
    })
    .then(response => response.json())
    .then(data => console.log(data))
}
