function upload(total)
{
	for(i=0;i<total;i+=10)
		{		$.ajax
				({
					type: "POST",
					url: "file.php",
					data: {"start":i},
					cache: false,
					success: function(html)
									{
										$("#result").html(html);
										var percent = (html/total*100).toString().concat("%");
										$(".meter > span").width(percent);
									} 
				});
				
		 }
	
}


  