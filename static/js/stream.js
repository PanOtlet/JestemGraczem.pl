function Stream(url) {

    var start = function () {
        $.get(url, function (data, status) {
            alert("Data: " + data + "\nStatus: " + status);
        });
    }

}