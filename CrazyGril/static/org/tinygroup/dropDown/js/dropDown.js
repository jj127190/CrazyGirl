/*下拉菜单项*/
$(function(){	
	$.Huihover('.dropDown');
	$(".dropDown_click .dropDown_A").click(function(){$(".dropDown").removeClass('open');if($(this).parents(".dropDown").hasClass('open')){$(this).parents(".dropDown").removeClass('open');}else{$(this).parents(".dropDown").addClass('open');} return false});
	$("body").click(function(){$(".dropDown").removeClass('open');});
	$(".dropDown-menu li a").click(function(){$(".dropDown").removeClass('open');});
	$(".dropDown_hover").hover(function(){$(this).addClass("open");},function(){$(this).removeClass("open");});
});