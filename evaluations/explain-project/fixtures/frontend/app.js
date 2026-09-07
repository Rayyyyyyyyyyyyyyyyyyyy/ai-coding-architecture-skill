const tasks = [{ id: 'sample', title: '試著新增一筆待辦' }];
const form = document.querySelector('#task-form');
const list = document.querySelector('#tasks');

function render() {
  list.replaceChildren(...tasks.map(task => {
    const item = document.createElement('li');
    item.textContent = task.title;
    return item;
  }));
}

form.addEventListener('submit', event => {
  event.preventDefault();
  const title = new FormData(form).get('title').trim();
  if (!title) return;
  tasks.push({ id: crypto.randomUUID(), title });
  render();
  form.reset();
});

render();
