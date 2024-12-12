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
      targetPage = 'games.html';
      break;
    case 4:
      targetPage = 'battleground.html';
      break;
    case 5:
      targetPage = 'contact.html';
      break;
    case 6:
      targetPage = '/login_1'
      break;
  }

  // Navigate to the selected page
  window.location.href = targetPage;
}
