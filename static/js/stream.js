var Stream = {
    template: '',
    start: function (url, urlEsport, mixer_url, twitch_url) {
        twitch_url = twitch_url.replace("_/", '');
        mixer_url = mixer_url.replace("_/", '');
        this.template = '<a class="carousel-item hoverable" href="' + twitch_url + '{{ 1 }}">' +
            '<img class="responsive-img" src="{{ 3 }}" alt="{{ 0 }}"></a>';
        this.templateESport = '<div class="col s12 m3">' + '<div class="card hoverable">' +
            '<div class="card-image">' + '<a href="' + twitch_url + '{{ 1 }}">' +
            '<img src="{{ 3 }}">' +
            '<span class="card-title hide-on-med-and-down">' +
            '<span class="new badge" data-badge-caption="na Twitch">{{ 0 }}</span>' +
            '</span></a></div></div></div>';
            // '<a class="carousel-item hoverable" href="' + twitch_url + '{{ 0 }}">' +
            // '<img class="responsive-img" src="{{ 3 }}" alt="{{ 0 }}"></a>';

        $('.carousel.carousel-slider').carousel({fullWidth: true});

        $.get(url, function (data, status) {
            Stream.generate(data, mixer_url, twitch_url);
        });

        $.get(urlEsport, function (data, status) {
            Stream.generateESport(data, mixer_url, twitch_url);
        });
    },
    generate: function (data, mixer_url, twitch_url) {
        for (var i = 0; i < data.length; i++) {
            $(".stream-container .carousel").append(Mustache.render(this.template, data[i]));
            console.log(data[i]);
        }

        $('.stream-container .carousel').carousel();
    },
    generateESport: function (data, mixer_url, twitch_url) {
        for (var i = 0; i < data.length; i++) {
            $(".esport-stream-container .esport-stream-row").append(Mustache.render(this.templateESport, data[i]));
            console.log(data[i]);
        }
    }
};