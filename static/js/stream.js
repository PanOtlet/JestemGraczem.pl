var test;
var Stream = {
    template: '',
    start: function (url, urlEsport, mixer_url, twitch_url) {
        this.checkExistsStorage();
        twitch_url = twitch_url.replace("_/", '');
        mixer_url = mixer_url.replace("_/", '');
        this.template = '<a class="carousel-item hoverable" href="' + twitch_url + '{{ 0 }}">' +
            '<img class="responsive-img" src="{{ 3 }}" alt="{{ 0 }}"></a>';
        if (localStorage['timestamp'] < Date.now() - 60)
            $.get(url, function (data, status) {
                test = data;
                localStorage['timestamp'] = Date.now();
                localStorage['streamData'] = JSON.stringify(data);
            });
        if (localStorage['timestampESport'] < Date.now() - 60)
            $.get(urlEsport, function (data, status) {
                test = data;
                localStorage['timestampESport'] = Date.now();
                localStorage['streamDataESport'] = JSON.stringify(data);
            });
        var jsonStreamData = JSON.parse(localStorage['streamData']);
        var jsonStreamDataESport = JSON.parse(localStorage['streamDataESport']);
        Stream.generate(jsonStreamData, mixer_url, twitch_url);
        Stream.generateESport(jsonStreamDataESport, mixer_url, twitch_url);
        $('.carousel.carousel-slider').carousel({fullWidth: true});
        $('.carousel').carousel();
    },
    generate: function (data) {
        for (var i = 0; i < data.length; i++) {
            $(".stream-container .carousel").append(Mustache.render(this.template, data[i]));
        }
    },
    generateESport: function (data) {
        for (var i = 0; i < data.length; i++) {
            $(".esport-stream-container .carousel").append(Mustache.render(this.template, data[i]));
        }
    },
    checkExistsStorage: function () {
        if (typeof localStorage['streamData'] === 'undefined') {
            localStorage['streamData']='';
        }

        if (typeof localStorage['timestamp'] === 'undefined'){
            localStorage['timestamp']=Date.now()/1000;
        }

        if (typeof localStorage['timestampESport'] === 'undefined'){
            localStorage['timestampESport']=Date.now()/1000;
        }

        if (typeof localStorage['streamDataESport'] === 'undefined'){
            localStorage['streamDataESport']='';
        }
    }
};