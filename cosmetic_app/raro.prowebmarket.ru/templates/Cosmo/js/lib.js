/*!
 * Bootstrap v3.3.5 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

/*!
 * Generated using the Bootstrap Customizer (http://getbootstrap.com/customize/?id=2b2230a7b5344c98477c)
 * Config saved to config.json and https://gist.github.com/2b2230a7b5344c98477c
 */
if("undefined"==typeof jQuery)throw new Error("Bootstrap's JavaScript requires jQuery");+function(t){"use strict";var e=t.fn.jquery.split(" ")[0].split(".");if(e[0]<2&&e[1]<9||1==e[0]&&9==e[1]&&e[2]<1||e[0]>3)throw new Error("Bootstrap's JavaScript requires jQuery version 1.9.1 or higher, but lower than version 3")}(jQuery),+function(t){"use strict";function e(e){var n=e.attr("data-target");n||(n=e.attr("href"),n=n&&/#[A-Za-z]/.test(n)&&n.replace(/.*(?=#[^\s]*$)/,""));var a=n&&t(n);return a&&a.length?a:e.parent()}function n(n){n&&3===n.which||(t(i).remove(),t(r).each(function(){var a=t(this),i=e(a),r={relatedTarget:this};i.hasClass("open")&&(n&&"click"==n.type&&/input|textarea/i.test(n.target.tagName)&&t.contains(i[0],n.target)||(i.trigger(n=t.Event("hide.bs.dropdown",r)),n.isDefaultPrevented()||(a.attr("aria-expanded","false"),i.removeClass("open").trigger(t.Event("hidden.bs.dropdown",r)))))}))}function a(e){return this.each(function(){var n=t(this),a=n.data("bs.dropdown");a||n.data("bs.dropdown",a=new s(this)),"string"==typeof e&&a[e].call(n)})}var i=".dropdown-backdrop",r='[data-toggle="dropdown"]',s=function(e){t(e).on("click.bs.dropdown",this.toggle)};s.VERSION="3.3.6",s.prototype.toggle=function(a){var i=t(this);if(!i.is(".disabled, :disabled")){var r=e(i),s=r.hasClass("open");if(n(),!s){"ontouchstart"in document.documentElement&&!r.closest(".navbar-nav").length&&t(document.createElement("div")).addClass("dropdown-backdrop").insertAfter(t(this)).on("click",n);var o={relatedTarget:this};if(r.trigger(a=t.Event("show.bs.dropdown",o)),a.isDefaultPrevented())return;i.trigger("focus").attr("aria-expanded","true"),r.toggleClass("open").trigger(t.Event("shown.bs.dropdown",o))}return!1}},s.prototype.keydown=function(n){if(/(38|40|27|32)/.test(n.which)&&!/input|textarea/i.test(n.target.tagName)){var a=t(this);if(n.preventDefault(),n.stopPropagation(),!a.is(".disabled, :disabled")){var i=e(a),s=i.hasClass("open");if(!s&&27!=n.which||s&&27==n.which)return 27==n.which&&i.find(r).trigger("focus"),a.trigger("click");var o=" li:not(.disabled):visible a",d=i.find(".dropdown-menu"+o);if(d.length){var l=d.index(n.target);38==n.which&&l>0&&l--,40==n.which&&l<d.length-1&&l++,~l||(l=0),d.eq(l).trigger("focus")}}}};var o=t.fn.dropdown;t.fn.dropdown=a,t.fn.dropdown.Constructor=s,t.fn.dropdown.noConflict=function(){return t.fn.dropdown=o,this},t(document).on("click.bs.dropdown.data-api",n).on("click.bs.dropdown.data-api",".dropdown form",function(t){t.stopPropagation()}).on("click.bs.dropdown.data-api",r,s.prototype.toggle).on("keydown.bs.dropdown.data-api",r,s.prototype.keydown).on("keydown.bs.dropdown.data-api",".dropdown-menu",s.prototype.keydown)}(jQuery),+function(t){"use strict";function e(e){return this.each(function(){var a=t(this),i=a.data("bs.tab");i||a.data("bs.tab",i=new n(this)),"string"==typeof e&&i[e]()})}var n=function(e){this.element=t(e)};n.VERSION="3.3.6",n.TRANSITION_DURATION=150,n.prototype.show=function(){var e=this.element,n=e.closest("ul:not(.dropdown-menu)"),a=e.data("target");if(a||(a=e.attr("href"),a=a&&a.replace(/.*(?=#[^\s]*$)/,"")),!e.parent("li").hasClass("active")){var i=n.find(".active:last a"),r=t.Event("hide.bs.tab",{relatedTarget:e[0]}),s=t.Event("show.bs.tab",{relatedTarget:i[0]});if(i.trigger(r),e.trigger(s),!s.isDefaultPrevented()&&!r.isDefaultPrevented()){var o=t(a);this.activate(e.closest("li"),n),this.activate(o,o.parent(),function(){i.trigger({type:"hidden.bs.tab",relatedTarget:e[0]}),e.trigger({type:"shown.bs.tab",relatedTarget:i[0]})})}}},n.prototype.activate=function(e,a,i){function r(){s.removeClass("active").find("> .dropdown-menu > .active").removeClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!1),e.addClass("active").find('[data-toggle="tab"]').attr("aria-expanded",!0),o?(e[0].offsetWidth,e.addClass("in")):e.removeClass("fade"),e.parent(".dropdown-menu").length&&e.closest("li.dropdown").addClass("active").end().find('[data-toggle="tab"]').attr("aria-expanded",!0),i&&i()}var s=a.find("> .active"),o=i&&t.support.transition&&(s.length&&s.hasClass("fade")||!!a.find("> .fade").length);s.length&&o?s.one("bsTransitionEnd",r).emulateTransitionEnd(n.TRANSITION_DURATION):r(),s.removeClass("in")};var a=t.fn.tab;t.fn.tab=e,t.fn.tab.Constructor=n,t.fn.tab.noConflict=function(){return t.fn.tab=a,this};var i=function(n){n.preventDefault(),e.call(t(this),"show")};t(document).on("click.bs.tab.data-api",'[data-toggle="tab"]',i).on("click.bs.tab.data-api",'[data-toggle="pill"]',i)}(jQuery),+function(t){"use strict";function e(e){var n,a=e.attr("data-target")||(n=e.attr("href"))&&n.replace(/.*(?=#[^\s]+$)/,"");return t(a)}function n(e){return this.each(function(){var n=t(this),i=n.data("bs.collapse"),r=t.extend({},a.DEFAULTS,n.data(),"object"==typeof e&&e);!i&&r.toggle&&/show|hide/.test(e)&&(r.toggle=!1),i||n.data("bs.collapse",i=new a(this,r)),"string"==typeof e&&i[e]()})}var a=function(e,n){this.$element=t(e),this.options=t.extend({},a.DEFAULTS,n),this.$trigger=t('[data-toggle="collapse"][href="#'+e.id+'"],[data-toggle="collapse"][data-target="#'+e.id+'"]'),this.transitioning=null,this.options.parent?this.$parent=this.getParent():this.addAriaAndCollapsedClass(this.$element,this.$trigger),this.options.toggle&&this.toggle()};a.VERSION="3.3.6",a.TRANSITION_DURATION=350,a.DEFAULTS={toggle:!0},a.prototype.dimension=function(){var t=this.$element.hasClass("width");return t?"width":"height"},a.prototype.show=function(){if(!this.transitioning&&!this.$element.hasClass("in")){var e,i=this.$parent&&this.$parent.children(".panel").children(".in, .collapsing");if(!(i&&i.length&&(e=i.data("bs.collapse"),e&&e.transitioning))){var r=t.Event("show.bs.collapse");if(this.$element.trigger(r),!r.isDefaultPrevented()){i&&i.length&&(n.call(i,"hide"),e||i.data("bs.collapse",null));var s=this.dimension();this.$element.removeClass("collapse").addClass("collapsing")[s](0).attr("aria-expanded",!0),this.$trigger.removeClass("collapsed").attr("aria-expanded",!0),this.transitioning=1;var o=function(){this.$element.removeClass("collapsing").addClass("collapse in")[s](""),this.transitioning=0,this.$element.trigger("shown.bs.collapse")};if(!t.support.transition)return o.call(this);var d=t.camelCase(["scroll",s].join("-"));this.$element.one("bsTransitionEnd",t.proxy(o,this)).emulateTransitionEnd(a.TRANSITION_DURATION)[s](this.$element[0][d])}}}},a.prototype.hide=function(){if(!this.transitioning&&this.$element.hasClass("in")){var e=t.Event("hide.bs.collapse");if(this.$element.trigger(e),!e.isDefaultPrevented()){var n=this.dimension();this.$element[n](this.$element[n]())[0].offsetHeight,this.$element.addClass("collapsing").removeClass("collapse in").attr("aria-expanded",!1),this.$trigger.addClass("collapsed").attr("aria-expanded",!1),this.transitioning=1;var i=function(){this.transitioning=0,this.$element.removeClass("collapsing").addClass("collapse").trigger("hidden.bs.collapse")};return t.support.transition?void this.$element[n](0).one("bsTransitionEnd",t.proxy(i,this)).emulateTransitionEnd(a.TRANSITION_DURATION):i.call(this)}}},a.prototype.toggle=function(){this[this.$element.hasClass("in")?"hide":"show"]()},a.prototype.getParent=function(){return t(this.options.parent).find('[data-toggle="collapse"][data-parent="'+this.options.parent+'"]').each(t.proxy(function(n,a){var i=t(a);this.addAriaAndCollapsedClass(e(i),i)},this)).end()},a.prototype.addAriaAndCollapsedClass=function(t,e){var n=t.hasClass("in");t.attr("aria-expanded",n),e.toggleClass("collapsed",!n).attr("aria-expanded",n)};var i=t.fn.collapse;t.fn.collapse=n,t.fn.collapse.Constructor=a,t.fn.collapse.noConflict=function(){return t.fn.collapse=i,this},t(document).on("click.bs.collapse.data-api",'[data-toggle="collapse"]',function(a){var i=t(this);i.attr("data-target")||a.preventDefault();var r=e(i),s=r.data("bs.collapse"),o=s?"toggle":i.data();n.call(r,o)})}(jQuery),+function(t){"use strict";function e(){var t=document.createElement("bootstrap"),e={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var n in e)if(void 0!==t.style[n])return{end:e[n]};return!1}t.fn.emulateTransitionEnd=function(e){var n=!1,a=this;t(this).one("bsTransitionEnd",function(){n=!0});var i=function(){n||t(a).trigger(t.support.transition.end)};return setTimeout(i,e),this},t(function(){t.support.transition=e(),t.support.transition&&(t.event.special.bsTransitionEnd={bindType:t.support.transition.end,delegateType:t.support.transition.end,handle:function(e){return t(e.target).is(this)?e.handleObj.handler.apply(this,arguments):void 0}})})}(jQuery);

// Скрипты шаблона 
$(function() {
	
	$('.dropdown-form').click(function(e) {
        e.stopPropagation();
    });

	// Меню
	var classes=[],
		a=$(".h_btn").click(function(e){
			e.preventDefault();
			a.not(this).toggleClass("open",false);

			$("html").removeClass(classes);

			if( $(this).toggleClass("open").hasClass("open") )
				$("html").addClass( $(this).prop("id")+"_open" );
		});

	a.each(function(){
		classes.push( $(this).attr("id")+"_open" );
	});

	classes=classes.join(" ");
	
	$('#closemenu').on('click', function(){
		$('html').removeClass('mainmenu_open');
		$('#mainmenu').removeClass('open');
		return false;
	});

	$('.soc_links a').on('click',function(){
	   var href = $(this).attr('href');
       var width  = 820;
       var height = 420;
       var left   = (screen.width  - width)/2;
       var top   = (screen.height - height)/2-100;   

       var auth_window = window.open(href, 'auth_window', "width="+width+",height="+height+",top="+top+",left="+left+"menubar=no,resizable=no,scrollbars=no,status=no,toolbar=no");
       return false;
	});

});