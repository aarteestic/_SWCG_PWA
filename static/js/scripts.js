  if ('serviceWorker' in navigator) {
      window.addEventListener('load', function() {
        navigator.serviceWorker.register("/sw.js", { scope: '/' })
        .then(function(registration) {
          // Registration was successful
          console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function(err) {
          // registration failed :(
          console.log('ServiceWorker registration failed: ', err);
        });
      });
    } 


function navigateTo(page) {
  let targetPage = '';

  switch (page) {
    case 1:
      targetPage = '/'; //the index thang
      break;
    case 2:
      targetPage = '/movies';
      break;
    case 3:
      targetPage = '/users';
      break;
    case 4:
      targetPage = 'battleground.html';
      break;
    case 5:
      targetPage = '/register';
      break;
    case 6:
      targetPage = '/login'
      break;
  }

  // Navigate to the selected page
  window.location.href = targetPage;
}
