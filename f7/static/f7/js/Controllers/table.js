var intervalID;


myApp.onPageInit('table-wait', function(page){
	//console.log('run');
	intervalID = setInterval(function(){
		 $$.ajax({
			url: 'api/dtable/'+table_id+'/wait_for_activation/', 
			method: 'get',
			success: function(result){
				//console.log(table_id);
				result = JSON.parse(result);
				if(result.status=='o'){
					mainView.router.loadPage('static/f7/html/table/main.html');
					clearInterval(intervalID);
				}	
			}
		})
	},500);
});


myApp.onPageInit('place-order', function(page){
		$$.ajax({
			url: 'api/menu/', 
			method: 'get',
			success: function(result){
				//console.log(result);
				result = JSON.parse(result);
				menu = result.results;
				for(var i=0;i<menu.length;i++){
					var menuName = menu[i].name;
					var menuPic = "static/f7/img/menu.jpg";
					var menuId = menu[i].id;
					var menuDesc = menu[i].description;
					var menuPrice = menu[i].price+' Baht';
					
					$$('#menu-list').append(
						'<div id="menu'+menuId+'"class="col-50 menu-item">'+
							 '<div class="card">'+
								'<div class="card-header">'+menuName+'</div>'+
									'<div class="card-content"> '+
									  '<div class="row">'+
										'<div class="col-33">'+
											'<img src="'+menuPic+'" alt="Menu">'+
										'</div>'+
											'<div class="col-66">'+
												'<div class="card-content-inner">'+menuDesc+'</div>'+
											'</div>'+
										'</div>'+
									'</div>'+
								'<div class="card-footer">'+menuPrice+'</div>'+
							 '</div>'+
						'</div>'
					);
				
					$$('#menu'+menuId).on('click', function () {
						var index = this.id.substr(4,1);
						index--;
						$$('.place-order-col ul').append(
								'<li>'+
								'<div class="item-content">'+
								  '<div class="item-inner"> '+
									'<div class="item-title">'+menu[index].name+'</div>'+
									'<div class="item-after">'+menu[index].price+'</div>'+
								  '</div>'+
								'</div>'+
								'</li>'
						);
						var total = parseInt($$('#menu-total').text());
						$$('#menu-total').text(total+menu[index].price);
						orderList.push(menu[index]);
						console.log(orderList);
					});
				}
			}
		})
});

function contains(a, obj) {
    for (var i = 0; i < a.length; i++) {
        if (a[i] === obj) {
            return true;
        }
    }
    return false;
}