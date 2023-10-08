const uniqueLinkTailings = new Set();
function process() { // invoke on page down
  const allLinks = document.querySelectorAll('a');
  allLinks.forEach(link => {
    const href = link.getAttribute('href');
    const regex = /\/user\/profile\/634a9047000000001802ddac\/(\w+)/;
    const match = href.match(regex);
    if (match && match[1]) {
      uniqueLinkTailings.add(match[1]);
    }
  });
}
