let form=document.querySelector("#formEdit")

fetch(`/api/student/${studentId}/`)
.then(res=>res.json())
.then(data=>{
    document.querySelector('#prenom').value=data.prenom
    document.querySelector('#note').value=data.note
})

form.addEventListener("submit",function(e){
    e.preventDefault()
    fetch(`/api/student/${studentId}/update/`,{
        method:"POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            prenom:document.querySelector('#prenom').value,
            note:document.querySelector("#note").value
        })
    })
    .then(res=>res.json())
    .then(data=>{
        alert('UPDATED')
        window.location.href="/student/list"
    })
})