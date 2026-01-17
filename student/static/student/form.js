
form=document.querySelector("#forms")

form.addEventListener('submit',function(e){
    e.preventDefault()
    let prenom=document.querySelector("#prenom").value
    let note=document.querySelector("#note").value

    fetch('/api/student/add',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            prenom:prenom,
            note:note
        })
    })
    .then(res=>res.json())
    .then(data=>{
        alert("student added successfully!")
        form.reset()
    })
})