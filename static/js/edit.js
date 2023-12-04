function send() {
    if (check()) {
        let form = document.getElementById("editWrite");
        form.submit();
    }
}

function check() {
    let pwd = document.getElementById("pwd").value;
    let get_pwd = document.getElementById("get_pwd").value;
    let check = false;

    if (pwd == get_pwd) {
        check = true;
    } else {
        alert("비밀번호가 일치하지 않습니다.");
    }

    return check;
}
