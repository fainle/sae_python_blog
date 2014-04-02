require.config({
    baseUrl:'/static/',
    paths:{
        "jquery":"js/jquery",
        "markitup":"markitup/jquery.markitup",
        "set":"markitup/sets/markdown/set"
    }
})

require(['jquery','markitup',"set"], function($, markItUp, mySettings){
    $(function() {
        $('#markItUp').markItUp(mySettings);
        //pic uplaod
        $("#upload_pic").click(function() {
            $.ajaxFileUpload ({
                url:"http://dilan.sinaapp.com/upload",
                fileElementId:"file",
                dataType:"json",
                success:function(data){
                    var url = "/file/" + data.name;
                    $("#pic_url").val(url)
                }
            })
        });
        //insert pic url
        $("#insert_pic").click(function() {
            src = $("#pic_url").val();
            alt = $("#pic_title").val();
            $.markItUp(
                { replaceWith:'<img src="'+src+'" alt="'+alt+'" title="'+alt+'"(!( class="[![Class]!]")!) />' }
            );
            $('#upload').modal('hide');
            return false;
        });
    });
});