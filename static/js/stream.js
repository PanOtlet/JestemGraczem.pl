var test;
var Stream = {
    template: '',
    start: function (url, mixer_url, twitch_url) {
        twitch_url = twitch_url.replace("_/", '');
        mixer_url = mixer_url.replace("_/", '');
        this.template = '<a class="carousel-item" href="' + twitch_url + '{{ 0 }}">' +
            '<img src="https://static-cdn.jtvnw.net/previews-ttv/live_user_{{ 1 }}-640x360.jpg"' +
            ' alt="{{ 0 }}"></a>';
        if (localStorage['timestamp'] < Date.now() - 60)
            $.get(url, function (data, status) {
                test = data;
                localStorage['timestamp'] = Date.now();
                localStorage['streamData'] = JSON.stringify(data);
            });
        Stream.generate(JSON.parse(localStorage['streamData']), mixer_url, twitch_url);
    },
    generate: function (data) {
        for (var i = 0; i < data.length; i++) {
            console.log('dupa');
            $(".stream-container .carousel").append(Mustache.render(this.template, data[i]));
        }
        $('.carousel.carousel-slider').carousel({fullWidth: true});
        $('.carousel').carousel();
    }
};