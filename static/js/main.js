





<script src="/static/js/bootstrap.min.js"></script>
<script src="/static/js/jquery.js"></script>
<script src="/static/markitup/jquery.markitup.js"></script>
<script src="/static/markitup/sets/markdown/set.js"></script>
<script src="/static/js/topic/jquery.upload.js"></script>
<script type="text/javascript">
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
</script>