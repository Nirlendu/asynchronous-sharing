
function urlify(text) {
    var urlRegex = /(https?:\/\/[^\s]+)/g;
    //var urlRegex = /^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i
    return text.match(urlRegex);
}

$(document).ready(function(){
    $('#textareaID1').keyup(function(){
        var x = null;
        var link = null;
        //console.log('HERE' + this.value);
        x = urlify(this.value);
        if(x != null){
            //console.log('At lo'x[0]);
            if(x != link){
                //console.log('X is here for function call' + x[0]);
                $(this).linkpreview(
                //preview.LinkPreview(
                {
                    url: x[0],
                    previewContainer: "#preview-container",
                });
                //console.log('X is here for function call' + x[0]);
                link = x[0];
            }
            
        }
    });
});

(function() {

    $ = window.jQuery;
    
    var LinkPreview = function(element, options) {
        this.init(element, options);
    };
    
    LinkPreview.prototype = {
        constructor: LinkPreview,

        options: null,
        url: null,

        $element: null,
        $previewContainer: null,
        $refreshButton: null,

        init: function(element, options) {

            this.$element = $(element);
            this.options = options;

            if (!this.$element) {
                return;
            }
            
            this.initPreviewContainer();
            this.emptyPreviewContainer();
            this.initUrlValue();

            if (options && options.refreshButton) {
                this.$refreshButton = $(options.refreshButton);

                var that = this;
                this.$refreshButton.on("click", function() {
                    that.emptyPreviewContainer();
                    that.initUrlValue();
                    that.getSource(that.url, that.renderPreview, that.renderError);
                });
            }

            this.getSource(this.url, this.renderPreview, this.renderError);
        },

        initPreviewContainer: function() {

            console.log('X is here at preview container');
            if (this.getOption("previewContainer")) {
                this.$previewContainer = $(this.options.previewContainer);
            } else {
                //this.$previewContainer = this.$element.parent();
                this.$previewContainer = this.$element.parent().find("#preview-container");
            }

            this.$previewContainer.addClass("link-preview");

            if (this.getOption("previewContainerClass")) {
                this.$previewContainer.addClass(this.options.previewContainerClass);
            } else {
                this.$previewContainer.addClass("well row-fluid");
            }
        },

        initUrlValue: function() {
            //console.log('X is here at url value');
            if (this.getOption("url")) {
                this.url = this.options.url;
            } else {
                this.url =
                    this.$element.attr("href") ||
                    this.$element.text() ||
                    this.$element.val();
            }
        },

        emptyPreviewContainer: function() {
            this.$previewContainer.empty();
        },

        getSource: function(url, onSuccess, onError) {

            //console.log('X is here at get source');
            if (!this.validateUrl(this.url)) {
                return;
            }

            if (typeof this.getOption("preProcess") === "function") {
                this.options.preProcess();
            }

            var that = this;

            //console.log('X is here at get source');

            $.ajax({
                url: url,
                type: "GET",
                success: function(data) {
                    onSuccess(this.url, data, that);
                    if (typeof that.getOption("onSuccess") === "function") {
                        that.options.onSuccess(data);
                    }
                },
                error: function() {
                    //this.emptyPreviewContainer;
                    onError(this.url, that);
                    if (typeof that.getOption("onError") === "function") {
                        that.options.onError();
                    }
                },
                complete: function() {
                    if (typeof that.getOption("onComplete") === "function") {
                        that.options.onComplete();
                    }
                }
            });
        },

        renderPreview: function(url, data, that) {
            
            // old request
            if (that.url !== url) {
                return;
            }

            that.emptyPreviewContainer();

            // html to lower case
            data = data.replace(/<\/?[A-Z]+[\w\W]*?>/g, function (m) {
                return m.toLowerCase();
            });

            // parse data to jQuery DOM object
            var dom = document.implementation.createHTMLDocument('');
            dom.body.innerHTML = data;
            var $dom = $(dom);
            
            // get components
            var title = that.findTitleInDom($dom),
                description = that.findDescriptionInDom($dom),
                image = that.findImageInDom($dom);

            //storing the link in database
            that.linkStore(url, title, description, image);

            // build dom elements
            var $title = $("<a></a>").attr("href", url).text(title),
                $description = $("<p></p>").text(description);

            var $spanRight;
            if (image) {
                var $image = $("<img></img>").attr("src", image),
                    $spanLeft = $("<div></div>").addClass("span4");
                $spanRight = $("<div></div>").addClass("span8");
                $spanLeft
                    .append($image);
                that.$previewContainer
                    .append($spanLeft);
            } else {
                $spanRight = $("<div></div>");
            }

            $spanRight
                .append($title)
                .append($description);
            that.$previewContainer
                .append($spanRight);
        },


        //storign the link data in database for future refrence
        linkStore : function(url, title, description, image){
            //putting them in DB first for future reference
            var csrftoken = $.cookie('csrftoken');
    
            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

            var formData = new FormData();

            formData.append('link_url',url);
            formData.append('link_name',title);
            formData.append('link_desc', description);
            formData.append('link_image', image);

            $.ajax({
                url: '/store/link/',
                type: 'POST',
                data: formData,
                cache: false,
                processData: false, // Don't process the files
                contentType: false, // Set content type to false as jQuery will tell the server its a query string request
                success: function(data, textStatus, jqXHR)
                {
                    if(typeof data.error === 'undefined')
                    {
                        console.log('It was stored!');
                    }
                    else
                    {
                        console.log('ERRORS: ' + data.error);
                    }
                },
                error: function(jqXHR, textStatus, errorThrown)
                {
                    console.log('ERRORS: ' + textStatus);
                }
            });

        },

        renderError: function(url, that) {

            //old request
            if (that.url !== url) {
                return;
            }

            that.emptyPreviewContainer();

            var $alert = $("<div></div>")
                .addClass("alert alert-error");

            if (that.getOption("errorMessage")) {
                $alert.text(that.options.errorMessage);
            } else {
                $alert.text("We are sorry we couldn't load the preview. Please check the URL.");
            }
                            
            that.$previewContainer.append($alert);
        },

        findTitleInDom: function($dom) {
            return $dom.find("meta[property='og:title']").attr("content") ||
                   $dom.find("title").text() ||
                   $dom.find("meta[name=title]").attr("content");
        },

        findDescriptionInDom: function($dom) {
            return  $dom.find("meta[property='og:description']").attr("content") ||
                    $dom.find("meta[name=description]").attr("content") ||
                    $dom.find("div .description").text();
        },

        findImageInDom: function($dom) {
            var imageSrc = $dom.find("meta[property='og:image'").attr("content") ||
                $dom.find("meta[itemprop=image]").attr("content") ||
                $dom.find("link[rel=image_src]").attr("content") ||
                this.findFirstImageInBody($dom.find("body"));

            // maybe the returned url is relative
            if (imageSrc && !this.validateUrl(imageSrc)) {

                var a = document.createElement("a");
                a.href = this.url;

                imageSrc = a.protocol + "//" + a.hostname + imageSrc;
            }

            return imageSrc;
        },

        findFirstImageInBody: function($body) {
            var result;

            var $images = $body.find("img[src]");

            var $img;
            $images.each(function() {
                $img = $(this);
                if ($img.attr("height") && $img.attr("height") > 40 &&
                    $img.attr("width") && $img.attr("width") > 40) {
                    result = this.src;
                    return false;
                }
            });

            return result;
        },

        getOption: function(name) {
            if (this.options && this.options[name]) {
                return this.options[name];
            } else {
                return null;
            }
        },

        validateUrl: function(value) {
            return (/^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i).test(value);
        }
    };

    $.fn.linkpreview = function (option) {
        return this.each(function () {
            var $this = $(this),
                data = $this.data('linkpreview'),
                options = typeof option === 'object' && option;
            $this.data('linkpreview', (data = new LinkPreview(this, $.extend({}, $.fn.linkpreview.defaults, options))));
        });
    };

    $.fn.linkpreview.defaults = {};
    
    $.fn.linkpreview.Constructor = LinkPreview;

})();

