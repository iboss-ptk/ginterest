// Export selectors engine
var $$ = Dom7;



myApp.onPageInit('reception-main', function(page){
    $$('.next-queue').on('click', function (){
        myApp.alert('yo yo','yo yo');
    });
});