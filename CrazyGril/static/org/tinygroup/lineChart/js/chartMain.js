/*!
 * ZUI - v1.3.0 - 2015-05-18
 * http://zui.sexy
 * Copyright (c) 2015 cnezsoft.com; Licensed MIT
 */
!
function(f, d) {
    if ("undefined" == typeof f) {
        throw new Error("ZUI requires jQuery")
    }
    f.zui || (f.zui = function(c) {
        f.isPlainObject(c) && f.extend(f.zui, c)
    });
    var g = 0;
    f.zui({
        uuid: function() {
            return 1000 * (new Date).getTime() + g++%1000
        },
        callEvent: function(h, l, k) {
            if (f.isFunction(h)) {
                "undefined" != typeof k && (h = f.proxy(h, k));
                var j = h(l);
                return l && (l.result = j),
                !(void 0 !== j && !j)
            }
            return 1
        },
        clientLang: function() {
            var j, h = d.config;
            if ("undefined" != typeof h && h.clientLang) {
                j = h.clientLang
            } else {
                var b = f("html").attr("lang");
                j = b ? b: navigator.userLanguage || navigator.userLanguage || "zh_cn"
            }
            return j.replace("-", "_").toLowerCase()
        }
    }),
    f.fn.callEvent = function(j, q, p) {
        var o = f(this),
        n = j.indexOf(".zui."),
        m = j;
        0 > n && p && p.name ? j += "." + p.name: m = j.substring(0, n);
        var l = f.Event(j, q);
        if ("undefined" == typeof p && n > 0 && (p = o.data(j.substring(n + 1))), p && p.options) {
            var k = p.options[m];
            f.isFunction(k) && f.zui.callEvent(p.options[m], l, p)
        }
        return l
    }
} (jQuery, window),
function(f) {
    var d = {
        zh_cn: '您的浏览器版本过低，无法体验所有功能，建议升级或者更换浏览器。 <a href="http://browsehappy.com/" target="_blank" class="alert-link">了解更多...</a>',
        zh_tw: '您的瀏覽器版本過低，無法體驗所有功能，建議升級或者更换瀏覽器。<a href="http://browsehappy.com/" target="_blank" class="alert-link">了解更多...</a>',
        en: 'Your browser is too old, it has been unable to experience the colorful internet. We strongly recommend that you upgrade a better one. <a href="http://browsehappy.com/" target="_blank" class="alert-link">Learn more...</a>'
    },
    g = function() {
        var j = this.isIE,
        h = j();
        if (h) {
            for (var k = 10; k > 5; k--) {
                if (j(k)) {
                    h = k;
                    break
                }
            }
        }
        this.ie = h,
        this.cssHelper()
    };
    g.prototype.cssHelper = function() {
        var h = this.ie,
        j = f("html");
        j.toggleClass("ie", h).removeClass("ie-6 ie-7 ie-8 ie-9 ie-10"),
        h && j.addClass("ie-" + h).toggleClass("gt-ie-7 gte-ie-8 support-ie", h >= 8).toggleClass("lte-ie-7 lt-ie-8 outdated-ie", 8 > h).toggleClass("gt-ie-8 gte-ie-9", h >= 9).toggleClass("lte-ie-8 lt-ie-9", 9 > h).toggleClass("gt-ie-9 gte-ie-10", h >= 10).toggleClass("lte-ie-9 lt-ie-10", 10 > h)
    },
    g.prototype.tip = function() {
        if (this.ie && this.ie < 8) {
            var b = f("#browseHappyTip");
            b.length || (b = f('<div id="browseHappyTip" class="alert alert-dismissable alert-danger alert-block" style="position: relative; z-index: 99999"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button><div class="container"><div class="content text-center"></div></div></div>'), b.prependTo("body")),
            b.find(".content").html(this.browseHappyTip || d[f.zui.clientLang() || "zh_cn"])
        }
    },
    g.prototype.isIE = function(h) {
        var c = document.createElement("b");
        return c.innerHTML = "<!--[if IE " + (h || "") + "]><i></i><![endif]-->",
        1 === c.getElementsByTagName("i").length
    },
    g.prototype.isIE10 = function() {
        return ! 1
    },
    f.zui({
        browser: new g
    }),
    f(function() {
        f("body").hasClass("disabled-browser-tip") || f.zui.browser.tip()
    })
} (jQuery),
+
function(d) {
    var c = function(f, g) {
        this.$ = d(f),
        this.options = this.getOptions(g),
        this.init()
    };
    c.DEFAULTS = {
        container: "body",
        move: !0
    },
    c.prototype.getOptions = function(b) {
        return b = d.extend({},
        c.DEFAULTS, this.$.data(), b)
    },
    c.prototype.init = function() {
        this.handleMouseEvents()
    },
    c.prototype.handleMouseEvents = function() {
        var A, z, y, x, w, v = this.$,
        u = "before",
        t = "drag",
        s = "finish",
        r = this.options,
        q = function(g) {
            if (r.hasOwnProperty(u) && d.isFunction(r[u])) {
                var f = r[u]({
                    event: g,
                    element: v
                });
                if (void 0 !== f && !f) {
                    return
                }
            }
            var b = d(r.container),
            h = v.offset();
            z = b.offset(),
            A = {
                x: g.pageX,
                y: g.pageY
            },
            y = {
                x: g.pageX - h.left + z.left,
                y: g.pageY - h.top + z.top
            },
            x = d.extend({},
            A),
            w = !1,
            v.addClass("drag-ready"),
            d(document).bind("mousemove", p).bind("mouseup", o),
            g.preventDefault(),
            r.stopPropagation && g.stopPropagation()
        },
        p = function(k) {
            w = !0;
            var g = k.pageX,
            f = k.pageY,
            b = {
                left: g - y.x,
                top: f - y.y
            };
            v.removeClass("drag-ready").addClass("dragging"),
            r.move && v.css(b),
            r.hasOwnProperty(t) && d.isFunction(r[t]) && r[t]({
                event: k,
                element: v,
                startOffset: y,
                pos: b,
                offset: {
                    x: g - A.x,
                    y: f - A.y
                },
                smallOffset: {
                    x: g - x.x,
                    y: f - x.y
                }
            }),
            x.x = g,
            x.y = f,
            r.stopPropagation && k.stopPropagation()
        },
        o = function(f) {
            if (d(document).unbind("mousemove", p).unbind("mouseup", o), !w) {
                return void v.removeClass("drag-ready")
            }
            var b = {
                left: f.pageX - y.x,
                top: f.pageY - y.y
            };
            v.removeClass("drag-ready").removeClass("dragging"),
            r.move && v.css(b),
            r.hasOwnProperty(s) && d.isFunction(r[s]) && r[s]({
                event: f,
                element: v,
                pos: b,
                offset: {
                    x: f.pageX - A.x,
                    y: f.pageY - A.y
                },
                smallOffset: {
                    x: f.pageX - x.x,
                    y: f.pageY - x.y
                }
            }),
            f.preventDefault(),
            r.stopPropagation && f.stopPropagation()
        };
        r.handle ? v.on("mousedown", r.handle, q) : v.on("mousedown", q)
    }/*,
    d.fn.draggable = function(b) {
        return this.each(function() {
            var j = d(this),
            h = j.data("zui.draggable"),
            g = "object" == typeof b && b;
            h || j.data("zui.draggable", h = new c(this, g)),
            "string" == typeof b && h[b]()
        })
    },
    d.fn.draggable.Constructor = c*/
} (jQuery);