var queue=0;
// Initialize your app
var myApp = new Framework7({
	modalTitle: '',
	swipePanel: 'right',
	template7Pages: true,
	template7Data: {
        // This context will applied for page/template with "about.html" URL
        'page:reception-main': {
            number:queue
        }
}
});

var table_id;
var orderList = [];
// Export selectors engine
var $$ = Dom7;

// Add view
var mainView = myApp.addView('.view-main', {
    // Because we use fixed-through navbar we can enable dynamic navbar
    dynamicNavbar: true
});


function init(){
    // run createContentPage func after link was clicked


    $$('#login-button').on('click', function () {
		var data = {
			"username": $$('#username').val(),
			"password": $$('#password').val()
		};
		myApp.showPreloader('Logging in...');
        $$.ajax({
			url: 'api/user/login/', 
			method: 'post',
			data: data,
			success: function(result){
				//console.log(result);
				myApp.hidePreloader();
				result = JSON.parse(result);
				table_id = result.table_id;
				if(result.isAuthenticated){
					switch(result.role_id){
						case 1: 
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
								else mainView.router.loadPage('static/f7/html/table/wait.html');
							}
						});
						break;
						case 2: mainView.router.loadPage('static/f7/html/table/wait.html'); break;
						case 3: mainView.router.loadPage('static/f7/html/table/wait.html'); break;
						default: myApp.alert('Role id error');
					}
				}else{
					 myApp.alert('Incorrect<br>username or password');
				}	
			},
			error: function(result){
				//console.log(result);
				myApp.hidePreloader();
				myApp.alert(result.statusText);
			}
		})
    });
	
	$$('.logOutButton').on('click', function () {
		myApp.actions([[{
			text: 'Log Out',
			color: 'red',
			onClick: function() {
				myApp.closePanel();
				mainView.goBack();
				mainView.hideNavbar();
			}
		}], [{
			text: 'Cancel',
			bold: true
		}]]);
	});
}

init();

// Callbacks to run specific code for specific pages
myApp.onPageInit('login-screen-embedded', function(page){});

// Generate dynamic page
var dynamicPageIndex = 0;
var mySwiper = myApp.swiper('.swiper-container', {
     pagination:'.swiper-pagination',
        direction: 'vertical'
     });
function createContentPage() {
	mainView.router.loadContent(
        '<!-- Top Navbar-->' +
        '<div class="navbar">' +
        '  <div class="navbar-inner">' +
        '    <div class="left"><a href="#" class="back link"><i class="icon icon-back"></i><span>Back</span></a></div>' +
        '    <div class="center sliding">Dynamic Page ' + (++dynamicPageIndex) + '</div>' +
        '  </div>' +
        '</div>' +
        '<div class="pages">' +
        '  <!-- Page, data-page contains page name-->' +
        '  <div data-page="dynamic-pages" class="page">' +
        '    <!-- Scrollable page content-->' +
        '    <div class="page-content">' +
        '      <div class="content-block">' +
        '        <div class="content-block-inner">' +
        '          <p>Here is a dynamic page created on ' + new Date() + ' !</p>' +
        '          <p>Go <a href="#" class="back">back</a> or go to <a href="services.html">Services</a>.</p>' +
        '        </div>' +
        '      </div>' +
        '    </div>' +
        '  </div>' +
        '</div>'
    );
	return;

}