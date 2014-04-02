require.config({
    baseUrl:'/static/',
    paths:{
        "jquery":"js/jquery",
        "markitup":"markitup/jquery.markitup",
    }
})

mySettings = {
	previewParserPath:	'',
	onShiftEnter:		{keepDefault:false, openWith:'\n\n'},
	markupSet: [
		{name:'First Level Heading', key:'1', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
		{name:'Second Level Heading', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
		{name:'Heading 3', key:'3', openWith:'### ', placeHolder:'Your title here...' },
		{name:'Heading 4', key:'4', openWith:'#### ', placeHolder:'Your title here...' },
		{name:'Heading 5', key:'5', openWith:'##### ', placeHolder:'Your title here...' },
		{name:'Heading 6', key:'6', openWith:'###### ', placeHolder:'Your title here...' },
		{separator:'---------------' },
		{name:'Bold', key:'B', openWith:'**', closeWith:'**'},
		{name:'Italic', key:'I', openWith:'_', closeWith:'_'},
		{separator:'---------------' },
		{name:'Bulleted List', openWith:'- ' },
		{name:'Numeric List', openWith:function(markItUp) {
			return markItUp.line+'. ';
		}},
		{separator:'---------------' },
		{name:'Picture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},
		{name:'Link', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
		{separator:'---------------'},
		{name:'Quotes', openWith:'> '},
		{name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
        {name:'Code', openWith:'<span><code>', closeWith:'</code></span>'},
		{separator:'---------------'},
		{name:'Preview', call:'preview', className:"preview"}
	]
}


miu = {
	markdownTitle: function(markItUp, char) {
		heading = '';
		n = $.trim(markItUp.selection||markItUp.placeHolder).length;
		for(i = 0; i < n; i++) {
			heading += char;
		}
		return '\n'+heading;
	}
}

require(['jquery','markitup'], function($){
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