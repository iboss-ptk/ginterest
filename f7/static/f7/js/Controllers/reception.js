// Export selectors engine
var $$ = Dom7;



myApp.onPageInit('reception-main', function(page){

    $$('.next-queue').on('click', function (){
        queue++;
        $$('.next-queue-num').text(queue);
        //myApp.alert('yo yo',queue);
    });
});