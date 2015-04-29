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
	},3000);
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
					var menuPic = "static/f7/img/menu-"+menu[i].id+".jpg";
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
						$$('.place-order-col').scrollTop($$('.place-order-col').height());
						orderList.push(menu[index]);
						//console.log(orderList);
					});
				}
			}
		})
		
	$$('.order-submit-buton').on('click', function () {
		for(var i in orderList){
			var data = {
				"orderlist_id": 	table_id,
				"status": "q",
				"comment": "...",
				"quantity": 1,
				"menu_id": orderList[i].id
			}
			$$.post('api/order/',data);
		}
		orderList = [];
		$$('#menu-total').text(0);
		$$('.place-order-col ul').children().remove();
		myApp.alert('Order submitted');
	});
});


myApp.onPageInit('table-history', function(page){
	var total = 0;
		$$.ajax({
			url: 'api/order/', 
			method: 'get',
			success: function(result){
				//console.log(result);
				result = JSON.parse(result);
				menu = result.results;
				for(var i=0;i<menu.length;i++){
					if(menu[i].orderlist_id == table_id){
					  $$.get('api/menu/'+menu[i].menu_id+'/',null,function(data){
						  data = JSON.parse(data);
						  $$('.history-list ul').append(
						  '<li>'+
							'<div class="item-content">'+
							  '<div class="item-media"><img src="static/f7/img/menu-'+data.id+'.jpg" width="44"/></div>'+
							  '<div class="item-inner">'+
								'<div class="item-title-row">'+
								  '<div class="item-title color-black">'+data.name+'</div>'+
								  '<div class="item-after">Amount: 1</div>'+
								'</div>'+
								'<div class="item-subtitle">Total: '+data.price+' Baht</div>'+
							  '</div>'+
							'</div>'+
						  '</li>'
						);
						total = total + data.price;
						$$('#history-total').text(total+' Baht');
					  });
					}
				}
			}
		})
		
});

myApp.onPageInit('table-check-out', function(page){
	var total = 0;
		$$.ajax({
			url: 'api/order/', 
			method: 'get',
			success: function(result){
				//console.log(result);
				result = JSON.parse(result);
				menu = result.results;
				for(var i=0;i<menu.length;i++){
					if(menu[i].orderlist_id == table_id){
					  $$.get('api/menu/'+menu[i].menu_id+'/',null,function(data){
						  data = JSON.parse(data);
						  $$('.check-out-list ul').append(
						  '<li>'+
							  '<div class="item-content">'+
								  '<div class="item-inner"> '+
									'<div class="row max-width">'+		
										'<div class="col-33 item-title">'+data.name+'</div>'+
										'<div class="col-33 item-after align-right">1</div>'+
										'<div class="col-33 item-after align-right">'+data.price+' Baht</div>'+
									'</div>'+
								  '</div>'+
							  '</div>'+
						  '</li>'
						);
						total = total + data.price;
						$$('#check-out-total').text(total+'.00 Baht');
						$$('#check-out-service').text(Math.round(total*0.1 * 100) / 100+' Baht');
						$$('#check-out-vat').text(Math.round(total *0.07 * 100) / 100+' Baht');
						$$('#check-out-grand-total').text(Math.round(total*1.17 * 100) / 100+' Baht');
					  });
					}
				}
			}
		});
	$$('.check-out-button').on('click' , function(){
		mainView.router.loadPage('static/f7/html/table/wait.html');
	});
});

function contains(a, obj) {
    for (var i = 0; i < a.length; i++) {
        if (a[i] === obj) {
            return true;
        }
    }
    return false;
}