var test;
var Stream = {
    start: function (url) {
        $.get(url, function (data, status) {
            test=data;
            Stream.generate(data)
        });
    },
    generate: function (data) {
        for (var i = 0; i < data.results.length; i++) {
        $(".stream-container .carousel").append(Mustache.render(
            '<a class="carousel-item" href="">' +
            '<img src="https://static-cdn.jtvnw.net/previews-ttv/live_user_{{ name }}-640x360.jpg"' +
            ' alt="{{ player.name }}"></a>'
            , data.result[i]))
        }
        // $(".stream-container .carousel").append(Mustache.render(
        //     '<a class="carousel-item" href="">' +
        //     '<img src="https://static-cdn.jtvnw.net/previews-ttv/live_user_{{ player.name }}-640x360.jpg"' +
        //     ' alt="{{ player.name }}"></a>'
        //     , view))
    }
};