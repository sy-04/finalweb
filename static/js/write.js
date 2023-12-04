function send() {
    if (check()) {
        let form = document.getElementById("form_write");
        form.submit();
    }
}

function check() {
    let title = document.getElementById("title").value;
    let name = document.getElementById("name").value;
    let pwd = document.getElementById("pwd").value;
    let content = document.getElementById("content").value;

    let str = "1234ABC";
    let check = /^[0-9]+$/;

    let submitCheck = false;

    if (title == "") {
        alert("제목을 입력하세요.");
        submitCheck = false;
    } else if (name == "") {
        alert("글쓴이를 입력하세요.");
        submitCheck = false;
    } else if (pwd == "") {
        alert("비밀번호를 입력하세요.");
        submitCheck = false;
    } else if (check.test(str)) {
        alert("비밀번호는 숫자만 입력 가능합니다.");
        submitCheck = false;
    } else if (content == "") {
        alert("내용을 입력하세요.");
        submitCheck = false;
    } else {
        submitCheck = true;
    }

    return submitCheck;
}
