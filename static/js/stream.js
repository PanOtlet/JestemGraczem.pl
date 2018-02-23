var Stream = {
    template: '',
    start: function (url, urlEsport, placeholder_image) {
        // this.template = '<div class="col s12 m4 l3">' + '<div class="card hoverable">' +
        //     '<div class="card-image">' + '<a id="{{ 1 }}" onclick="Stream.open_stream(this.id)" href="#">' +
        //     '<img data-src="{{ 3 }}" src="' + placeholder_image + '">' +
        //     '<span class="card-title hide-on-med-and-down">' +
        //     '<span class="new badge blue-gray" data-badge-caption="">{{ 0 }} {{ 2 }} {{ 5 }}</span>' +
        // '</span></a></div></div></div>';
        this.template =
            '<div class="col s12 m4 l3"><div class="card"><div class="card-image waves-effect waves-block waves-light">' +
            '<img class="activator" data-src="{{ 3 }}" src="' + placeholder_image + '"></div><div class="card-content">' +
            '<span class="card-title activator grey-text text-darken-4">{{ 0 }}</span>' +
            '<p><a id="{{ 1 }}" onclick="Stream.open_stream(this.id)" href="#">Oglądaj</a></p>' +
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
    generate: function (data) {
        for (var i = 0; i < data.length; i++) {
            $(".stream-container-row").append(Mustache.render(this.template, data[i]));
        }
        $("#stream_loading").remove();
    },
    generateESport: function (data) {
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                $(".esport-stream-row").append(Mustache.render(this.template, data[i]));
            }
            $("#esport_loading").remove();
        } else {
            $(".esport-stream-row").remove();
        }
    },
    lazyLoad: function () {
        var images = document.querySelectorAll('img[data-src]');
        lazyload(images);
    },
    open_stream: function (id) {
        $('#stream_url').attr("src", "https://player.twitch.tv/?channel=" + id);
        $('#modal').modal('open');
    }
};