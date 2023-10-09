document.getElementById('sub').onclick = () => {
    pname = document.getElementById('pname').value
    prs = document.getElementById('prs').value
    pre = document.getElementById('pre').value
    check = document.getElementById('agree').checked
    if (pname===''){
        alert("Fill The Product Name Please");
    }
    if (prs===''){
        alert("Fill The Product Starting Price")
    }
    if (pre===''){
        alert("Fill The product Ending Price");
    }
    if (check===false){
        alert("Please agree to Terms and Conditions");
    }
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
