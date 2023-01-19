function getCSRFToken() {
  const name = "csrftoken";
  let cookieValue = null;

  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();

      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}


// TODO: show popup at right-top when save is success or not
function popup() {
}

function getFormContent() {
  const title = document.getElementById("title");
  const content = document.getElementById("content");
  return [title.value, content.value];
}

// notebook id from edit.html
const data = document.currentScript.dataset;
const notebookId = data.id

function saveNotebook() {
  // get csrftoken
  const csrf_token = getCSRFToken();

  // edit notebook url
  const url = `/notebook/edit/${notebookId}/`;

  const [title, content] = getFormContent();

  const formData = new FormData();
  formData.append("title", title);
  formData.append("content", content);

  fetch(url, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": csrf_token,
    },
  }).then(response => {
    if (!response.ok) {
      // TODO: show error popup - can't connect server
      console.log("hoge");
    }
  }).catch(error => {
    // console.log(error);
    // TODO: show error popup - something wrong with
  });
}

// don't show popup when run automatic save because it's annoying.
const interval = 20 * 1000;
setInterval(saveNotebook, interval);

// shortcut: Ctrl-s: save a notebook
document.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key === 's') {
    event.preventDefault();
    saveNotebook();
    popup();
  }
});

