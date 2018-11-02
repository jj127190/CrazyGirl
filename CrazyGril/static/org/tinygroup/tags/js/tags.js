$(function(){	
	/*tag标签*/
	var $that = $(".hui-tags"),
		$taginput = $that.find(".hui-tags-input"),
		$taglable = $that.find(".hui-tags-lable"),
		$tagswp = $that.find(".hui-tags-iptwrap"),
		$taglist = $that.find(".hui-tags-list"),
		$taghas = $taglist.find(".hui-tags-has"),
		time1;
	$taglable.show();
	$taginput.val("");
	$taginput.blur(function(){
		time1 = setTimeout(function(){
			$taglist.slideUp();
		}, 400);
	});
	$taginput.focus(function(){
		clearTimeout(time1);
	});
	$that.on("click",function(){	
		$taginput.focus();
		$taglist.slideDown();
	});
	$taginput.on("keydown",function(event){
		$taglable.hide();
		var v = trim($taginput.val());
		if(v!=''){
			if(event.keyCode==13||event.keyCode==108||event.keyCode==32){
				v = trim($taginput.val());
				var haven = false;
				$.each($('.hui-tags-token'), function(i,n){
					if ($(n).text() == v) {
						haven = true;
						return false;
					}
				});
				if (!haven) {
					$('<span class="hui-tags-token">'+v+'</span>').insertBefore($tagswp);
				}
				$taginput.val("");
			}
		}else{
			if(event.keyCode==8){
				if($that.find(".hui-tags-token:last").length>0){$that.find(".hui-tags-token:last").remove();}
				else{
					$taglable.show();
				}
				
			}
		}	
	});
		
	$taghas.find("span").click(function(){
		var taghasV = $(this).text();
		$('<span class="hui-tags-token">'+taghasV+'</span>').insertBefore($tagswp);
		$taginput.focus();
	});
	$(document).on("click",".hui-tags-token",function(){
		$(this).remove();
		if($that.find(".hui-tags-token:last").length==0){
			$taglable.show();
		}
	});
	
	
});
$(function(){
/*tag标签*/
	var tags_a = $(".tags a");
	tags_a.each(function(){
		var x = 9;
		var y = 0;
		var rand = parseInt(Math.random() * (x - y + 1) + y);
		$(this).addClass("tags"+rand);
	});
});