webpackJsonp([3], { 382: function(t, e, n) { "use strict";
        Object.defineProperty(e, "__esModule", { value: !0 }); var i = n(398),
            o = n.n(i); for (var r in i) "default" !== r && function(t) { n.d(e, t, function() { return i[t] }) }(r); var s = n(39),
            l = Object(s.a)(o.a, void 0, void 0, !1, null, null, null);
        l.options.__file = "src/js/vue-components/SpotlightsRecent.vue", e.default = l.exports }, 398: function(t, e, n) { "use strict";
        (function(t) {
            function i(t) { return t && t.__esModule ? t : { default: t } } Object.defineProperty(e, "__esModule", { value: !0 }); var o = i(n(415)),
                r = i(n(417));
            e.default = { el: "#node-spotlight", data: function() { return { recentSpotlights: [], theLinkToSpotlightArchive: [] } }, components: { "spotlights-archive-link": o.default, "spotlight-item": r.default }, mounted: function() { var e = this,
                        n = this.$el.dataset.viewingspotlight,
                        i = window.location.pathname,
                        o = i;
                    i.indexOf("index.html") >= 0 && (o = i.substring(0, i.lastIndexOf("/") + 1));
                    t.getJSON("/spotlights-export/recent/?_format=json").done(function(t) { var i = [];
                        t.forEach(function(t) { t.url != o && t.url + "/" != o && t.title != n && i.push(t) }), e.recentSpotlights = i, 0 != t.length && (e.theLinkToSpotlightArchive = "/archive" + t[0].url) }) } } }).call(e, n(18)) }, 399: function(t, e, n) { "use strict";
        Object.defineProperty(e, "__esModule", { value: !0 }); var i = function(t) { return t && t.__esModule ? t : { default: t } }(n(70));
        e.default = { props: ["linktospotlightsarchive"], methods: { fireGAEvent: function(t, e) { i.default.linkClickEvent(t, e) } } } }, 400: function(t, e, n) { "use strict";
        Object.defineProperty(e, "__esModule", { value: !0 }); var i = function(t) { return t && t.__esModule ? t : { default: t } }(n(70));
        e.default = { props: ["title", "url", "datelabel", "theme", "placeholder", "linkcolor", "bgcolor"], data: function() { return { bgColor: "", txtColor: "" } }, computed: { formattedTitle: function() { return "spotlight-recirc__item " + this.theme }, hashURL: function() { return this.isToday() ? "/" : this.url + "/#main" }, formattedDate: function() { return this.isToday() ? "Today" : this.datelabel }, onMouseOverOutput: function() { return "this.style.background='" + this.linkcolor + "'" } }, methods: { isToday: function() { var t = new Date,
                        e = t.getDate(),
                        n = t.getMonth(); return e < 10 && (e = "0" + e), this.datelabel == ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"][n] + " " + e }, fireGAEvent: function(t, e) { i.default.linkClickEvent(t, e) }, mouseOver: function() { this.bgColor = "#" + this.linkcolor, this.txtColor = "#" + this.bgcolor }, mouseOut: function() { this.bgColor = "", this.txtColor = "" } } } }, 415: function(t, e, n) { "use strict";
        Object.defineProperty(e, "__esModule", { value: !0 }); var i = n(399),
            o = n.n(i); for (var r in i) "default" !== r && function(t) { n.d(e, t, function() { return i[t] }) }(r); var s = n(416),
            l = n(39),
            u = Object(l.a)(o.a, s.a, s.b, !1, null, null, null);
        u.options.__file = "src/js/vue-components/SpotlightsArchiveLink.vue", e.default = u.exports }, 416: function(t, e, n) { "use strict";
        n.d(e, "a", function() { return i }), n.d(e, "b", function() { return o }); var i = function() { var t = this,
                    e = t.$createElement,
                    n = t._self._c || e; return t.linktospotlightsarchive ? n("div", { staticClass: "spotlight-newsletter-cta" }, [n("div", { staticClass: "spotlight-newsletter-cta-inner" }, [n("h4", { staticClass: "spotlight-newsletter-cta__h" }, [t._v("Want more?")]), t._v(" "), n("p", { staticClass: "spotlight-newsletter-cta__text" }, [t._v("\n    Explore "), n("a", { attrs: { href: t.linktospotlightsarchive }, on: { click: function(e) { t.fireGAEvent(t.linktospotlightsarchive, "Footer Link") } } }, [t._v("past Spotlights")]), t._v(", or \n    "), n("a", { attrs: { href: "/subscribe" }, on: { click: function(e) { t.fireGAEvent("/subscribe", "Footer Link") } } }, [t._v("subscribe")]), t._v(" to receive daily or weekly doses of MIT in your inbox.")])]), t._v(" "), n("a", { staticClass: "spotlight-newsletter-cta__button", attrs: { href: "/subscribe" }, on: { click: function(e) { t.fireGAEvent("/subscribe", "Footer Link") } } }, [t._v("Subscribe")])]) : t._e() },
            o = [];
        i._withStripped = !0 }, 417: function(t, e, n) { "use strict";
        Object.defineProperty(e, "__esModule", { value: !0 }); var i = n(400),
            o = n.n(i); for (var r in i) "default" !== r && function(t) { n.d(e, t, function() { return i[t] }) }(r); var s = n(418),
            l = n(39),
            u = Object(l.a)(o.a, s.a, s.b, !1, null, null, null);
        u.options.__file = "src/js/vue-components/SpotlightsRecentListItem.vue", e.default = u.exports }, 418: function(t, e, n) { "use strict";
        n.d(e, "a", function() { return i }), n.d(e, "b", function() { return o }); var i = function() { var t = this,
                    e = t.$createElement,
                    n = t._self._c || e; return n("li", { class: t.formattedTitle }, [n("a", { staticClass: "spotlight-recirc__link", style: { background: t.bgColor, color: t.txtColor }, attrs: { href: t.hashURL }, on: { mouseover: t.mouseOver, mouseleave: t.mouseOut, click: function(e) { t.fireGAEvent(t.url, "Recent Spotlight Link") } } }, [n("div", { staticClass: "spotlight-recirc__hgroup" }, [n("h3", { staticClass: "spotlight-recirc__title", domProps: { innerHTML: t._s(t.title) } }, [t._v(t._s(t.title))]), t._v(" "), n("p", { staticClass: "spotlight-recirc__date" }, [t._v(t._s(t.formattedDate))])])])]) },
            o = [];
        i._withStripped = !0 } });