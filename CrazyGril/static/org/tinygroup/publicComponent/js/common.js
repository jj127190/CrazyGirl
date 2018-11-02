function launchFullScreen(element) {
    var request;
    if (!$('body').hasClass("full-screen")) {
      request = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen ||	element.msRequestFullScreen;
      if(typeof request!="undefined" && request){
          request.call(element);
      }else{
          alert("你的浏览器不支持，请按F11进行全屏预览");
          return false;
      }
    } else {
      request = document.cancelFullScreen|| document.webkitCancelFullScreen || document.mozCancelFullScreen || document.msCancelFullScreen || document.exitFullscreen;
      if(typeof request!="undefined" && request){
          request.call(document);
      }
    }
    $('body').toggleClass("full-screen");
}
/*选项卡*/
jQuery.Huihover =function(obj) {
	$(obj).hover(function(){$(this).addClass("hover");},function(){$(this).removeClass("hover");});
};
jQuery.Huitab =function(tabBar,tabCon,class_name,tabEvent,i){
	var $tab_menu=$(tabBar);
	// 初始化操作
	$tab_menu.removeClass(class_name);
	$(tabBar).eq(i).addClass(class_name);
	$(tabCon).hide();
	$(tabCon).eq(i).show();

	$tab_menu.bind(tabEvent,function(){
		$tab_menu.removeClass(class_name);
		$(this).addClass(class_name);
		var index=$tab_menu.index(this);
		$(tabCon).hide();
		$(tabCon).eq(index).show();
	});
}
jQuery.Huifocusblur = function(obj) {
	$(obj).focus(function() {$(this).addClass("focus").removeClass("inputError");});
	$(obj).blur(function() {$(this).removeClass("focus");});
};

/**异步加载url的函数*/
function loadLink(a, b, c , d) {
	var loadtype = "POST";
	if(d){
		loadtype = d;
	}
	var paramdata = {};
	if(c){
		paramdata = c;
	}
    $.ajax({
        type: loadtype,
        url: a,
        data: paramdata,
        dataType: "html",
        cache: !0,
        beforeSend: function() {
            if ($.navAsAjax && $(".google_maps")[0] && b[0] == b[0]) {
                var a = $(".google_maps"),
                c = 0;
                a.each(function() {
                    c++;
                    var b = document.getElementById(this.id);
                    c == a.length + 1 || b && b.parentNode.removeChild(b)
                })
            }
            if ($.navAsAjax && $(".dataTables_wrapper")[0] && b[0] == b[0]) {
                var d = $.fn.dataTable.fnTables(!0);
                $(d).each(function() {
                    $(this).dataTable().fnDestroy()
                })
            }
            if ($.navAsAjax && $.intervalArr.length > 0 && b[0] == b[0]) for (; $.intervalArr.length > 0;) clearInterval($.intervalArr.pop());
            b.html('<h1 class="ajax-loading-animation"><i class="fa fa-cog fa-spin"></i> 加载...</h1>'),
            b[0] == b[0] && (drawBreadCrumb(), $("html").animate({
                scrollTop: 0
            },
            "fast"))
        },
        success: function(a) {
            b.css({
                opacity: "0.0"
            }).html(a).delay(50).animate({
                opacity: "1.0"
            },
            300)
        },
        error: function() {
            b.html('<h4 class="ajax-loading-error"><i class="fa fa-warning txt-color-orangeDark"></i> Error 404! Page not found.</h4>')
        },
        async: !0
		//async: true
    })
}
if (Storage) {
	Storage.prototype.setObject = function(key, value) {
	  this.setItem(key, JSON.stringify(value));
	};


	Storage.prototype.getObject = function(key) {
	  return this.getItem(key) && JSON.parse(this.getItem(key));
	};
}