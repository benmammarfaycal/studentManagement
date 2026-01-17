console.log('loaded')
let list=document.querySelector('#liste')

fetch('/api/student/shows')
.then(res=>res.json())
.then(data=>{
    data.forEach(student=>{
        let li=document.createElement('li')
        li.innerHTML=`Prenom:${student.prenom}-Note:${student.note}
            <button class='del'>Delete</button>
            <a href='/student/${student.id}/edit/'>Update</a>`

        let btndel=li.querySelector('.del')
        btndel.addEventListener('click',function(){
            fetch(`/api/student/${student.id}/delete`,{
                method:'DELETE',
            })
            .then(res=>res.json())
            .then(data=>{
                li.remove()
            })
        })
        list.appendChild(li)
    })
})