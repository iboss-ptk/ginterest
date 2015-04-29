myApp.onPageInit('table-wait', function(page){
	console.log('run');
	setInterval(function(){
		 $$.ajax({
			url: 'api/dtable/'+table_id+'/wait_for_activation/', 
			method: 'get',
			success: function(result){
				console.log(table_id);
				result = JSON.parse(result);
				if(result.status=='o'){
					mainView.router.loadPage('static/f7/html/table/main.html');
				}	
			}
		})
	},1000);
});