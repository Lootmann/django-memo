/**
 * focus search_form when hit Ctrl+F
 * */
function focus() {
  const search_form = document.getElementById("search_form");
  search_form.focus();
}

document.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key === 'f') {
    event.preventDefault();
    focus();
  }
});
