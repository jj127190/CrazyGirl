function CheckIsValidDomain(domain) {
    var re = new RegExp(/^((?:(?:(?:\w[\.\-\+]?)*)\w)+)((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$/);
    return domain.match(re);
}

function goBack() {
    history.go(-1);
}

function closeAllLayer() {
    layer.closeAll()
}


function init_button(init_url){
    var task_id = $("#task_id").val();
    // var init_url = "{% url 'webmanage:ajax_init_button'%}";
    $.post(init_url,{'id':task_id,'csrftoken':csrftoken},
        function(data){
            if(data == 1){
                $("#approve").attr("disabled", true);
                $("#execute").attr("disabled", false);
                $("#reject").attr("disabled", false);
            } else if(data == 0){
                $("#approve").attr("disabled", false);
                $("#execute").attr("disabled", true);
                $("#reject").attr("disabled", false);
            } else if(data == 2){
                $("#approve").attr("disabled", true);
                $("#execute").attr("disabled", true);
                $("#reject").attr("disabled", true);
            } else{
                $("#approve").attr("disabled", true);
                $("#execute").attr("disabled", false);
                $("#reject").attr("disabled", false);
            }
        },"json");
}

function changeaction(obj) {
   var doing = $(obj).attr("id");
    $("#action").val(doing);
    if (doing=="reject"){
        layer.prompt({
        formType: 2,
        title: '请输入驳回原因',

        }, function (value, index, elem) {
                $("#remark").val(value);
                layer.close(index);
                $("#selfform").submit()
        });
    }else{
        // alert(doing);
        $("#selfform").submit()
    }

}