var Stream = {
    template: '',
    start: function (url, urlEsport, mixer_url, twitch_url) {
        twitch_url = twitch_url.replace("_/", '');
        mixer_url = mixer_url.replace("_/", '');
        this.template = '<div class="col s12 m4 l3">' + '<div class="card hoverable">' +
            '<div class="card-image">' + '<a href="' + twitch_url + '{{ 1 }}">' +
            '<img src="{{ 3 }}">' +
            '<span class="card-title hide-on-med-and-down">' +
            '<span class="new badge red" data-badge-caption="">{{ 0 }}</span>' +
            '</span></a></div></div></div>';

        $.get(url, function (data, status) {
            Stream.generate(data, mixer_url, twitch_url);
        });

        $.get(urlEsport, function (data, status) {
            Stream.generateESport(data, mixer_url, twitch_url);
        });
    },
    generate: function (data, mixer_url, twitch_url) {
        for (var i = 0; i < data.length; i++) {
            $(".stream-container-row").append(Mustache.render(this.template, data[i]));
        }
        $("#stream_loading").remove();
    },
    generateESport: function (data, mixer_url, twitch_url) {
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                $(".esport-stream-row").append(Mustache.render(this.template, data[i]));
            }
            $("#esport_loading").remove();
        } else {
            $(".esport-stream-row").remove();
        }
    }
};