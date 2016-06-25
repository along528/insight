function complete(){
	currentQuery=$("#agency_query").val()
	$.ajax({
		url: "/search",
		data: {agency_query: currentQuery},
		success: function(results){
			$("#results_search").html(results);
		}
		});
}

