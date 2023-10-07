document.getElementById('sub').onclick = () => {
    const pp = document.getElementById('sel').value
    if (pp === '1'){
        location.href = "mobile.html";
    } else if (pp === '2'){
        location.href = "laptop.html";
    } else if (pp === '3'){
        location.href = "tv.html";
    } else{
        alert("Please Select An Option")
    }
}
