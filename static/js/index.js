function send(e) {
    let title_id = document
        .getElementById(e.getAttribute("id"))
        .getAttribute("id");
    let form_id = "form_" + title_id;
    let form = document.getElementById(form_id);

    form.submit();
}
