var test;
var Stream = {
    start: function (url, mixer_url, twitch_url) {
        $.get(url, function (data, status) {
            test = data;
            Stream.generate(data, mixer_url, twitch_url)
        });
    },
    generate: function (data, mixer_url, twitch_url) {
        twitch_url = twitch_url.replace("_/",'');
        mixer_url = mixer_url.replace("_/",'');
        if (data.length === 0) {
            $(".stream-container .carousel").append('<div class="video-container">' +
                '<iframe allowfullscreen ' +
                'src="https://player.twitch.tv/?channel=monstercat" ' +
                'frameborder="0"></iframe>' +
                '</div>')
        } else {
            for (var i = 0; i < data.length; i++) {
                console.error(data[i][0]);
                $(".stream-container .carousel").append(Mustache.render(
                    '<a class="carousel-item" href="'+ twitch_url +'{{ 0 }}">' +
                    '<img src="https://static-cdn.jtvnw.net/previews-ttv/live_user_{{ 1 }}-640x360.jpg"' +
                    ' alt="{{ 0 }}"></a>'
                    , data[i]));
            }
            $('.carousel.carousel-slider').carousel({fullWidth: true});
            $('.carousel').carousel();
        }
        // $(".stream-container .carousel").append(Mustache.render(
        //     '<a class="carousel-item" href="">' +
        //     '<img src="https://static-cdn.jtvnw.net/previews-ttv/live_user_{{ player.name }}-640x360.jpg"' +
        //     ' alt="{{ player.name }}"></a>'
        //     , view))
    }
};