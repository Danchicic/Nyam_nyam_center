const submitButton = document.getElementById("submitButton");
submitButton.addEventListener('click', function () {
    fetch(document.getElementById("form").getAttribute("action"), {
        method: 'POST', headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].getAttribute('value')
        }, body: JSON.stringify({"ing_name": "new_value_or_delete"})

    }).then(r => {

        if (r.ok) {
            let json = r.json();
            console.log(json);
            json.then(data => {
                let pageSource = data.HtmlPage;
                document.open();
                document.write(pageSource);
                document.close();
            });


        } else {
            alert("Ошибка HTTP: " + r.status);

        }
    });
});