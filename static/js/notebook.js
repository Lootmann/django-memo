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


// show popup at right-top whether saving is success or not
function popup(status) {
  let message;
  const p = document.getElementById("popup");

  if (status === "success") {
    message = "Success to Save :^)"
  } else if (status === "error") {
    message = "Fail to Save D:"
  } else {
    return;
  }

  p.textContent = message;
  p.classList.add(status);
  setTimeout(() => {
    p.classList.remove(status);
  }, 1000);
}

function getFormContent() {
  const title = document.getElementById("title");
  const content = document.getElementById("content");
  return [title.value, content.value];
}

// notebook id from edit.html
const data = document.currentScript.dataset;
const notebookId = data.id

function saveNotebook(show_message = true) {
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
    if (show_message) {
      if (response.ok) {
        popup("success");
      } else {
        popup("error");
      }
    }
  }).catch(error => {
    // TODO: show error popup - something wrong with
    if (show_message) {
      popup("error");
    }
  });
}

// don't show popup when run automatic save because it's annoying.
let autosaveTimer = setInterval(() => {
  saveNotebook(false)
}, 20 * 1000);

// shortcut: Ctrl-s: save a notebook
document.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key === 's') {
    event.preventDefault();
    saveNotebook();

    // refresh timer
    clearInterval(autosaveTimer);
    autosaveTimer = setInterval(() => {
      saveNotebook(false)
    }, 30 * 1000);
  }
});

