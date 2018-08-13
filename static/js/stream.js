let Stream = {
    template: '',
    start: function (url, urlEsport, placeholder_image) {
        this.template =
            '<div class="col s12 m4 l3"><div class="card"><div class="card-image waves-effect waves-block waves-light">' +
            '<img class="activator" data-src="{{ 3 }}" src="' + placeholder_image + '"></div><div class="card-content">' +
            '<span class="card-title activator grey-text text-darken-4">{{ 0 }}</span>' +
            '<p id="{{ 1 }}" onclick="Stream.open_stream(this.id)" style="cursor: pointer">Oglądaj</p>' +
            '</div>' +
            '<div class="card-reveal">' +
            '<span class="card-title grey-text text-darken-4">{{ 0 }}<i class="material-icons right">Zamknij</i>' +
            '<p>Widzów: {{ 5 }}<br>Gra: {{ 2 }}</p>' +
            '<p>{{ 6 }}</p>' +
            '</div></div></div>';

        $.get(url, function (data, status) {
            Stream.generate(data, placeholder_image);
        });

        $.get(urlEsport, function (data, status) {
            Stream.generateESport(data, placeholder_image);
        });

        $(document).ajaxComplete(function () {
            Stream.lazyLoad();
        });
    },
    startIndex: function (url) {
        this.template = '<div class="col m6 s12" style="cursor: pointer">' +
            '<img id="{{ 1 }}" onclick="Stream.open_stream(this.id)" src="{{ 3 }}" class="responsive-img">' +
            '</div>';

        $.get(url, function (data, status) {
            Stream.generatePartner(data);
        });
    },
    generate: function (data) {
        for (let i = 0; i < data.length; i++) {
            $(".stream-container-row").append(Mustache.render(this.template, data[i]));
        }
        $("#stream_loading").remove();
    },
    generatePartner: function (data) {
        for (let i = 0; i < data.length; i++) {
            $(".stream-row").append(Mustache.render(this.template, data[i]));
        }
    },
    generateESport: function (data) {
        if (data.length !== 0) {
            for (let i = 0; i < data.length; i++) {
                $(".esport-stream-row").append(Mustache.render(this.template, data[i]));
            }
            $("#esport_loading").remove();
        } else {
            $(".esport-stream-row").remove();
        }
    },
    lazyLoad: function () {
        if (typeof lazyload !== 'undefined') {
            let images = document.querySelectorAll('img[data-src]');
            lazyload(images);
        }
    },
    open_stream: function (id) {
        $('#stream_url').attr("src", "https://player.twitch.tv/?channel=" + id);
        $('#modal').modal('open');
    }
};