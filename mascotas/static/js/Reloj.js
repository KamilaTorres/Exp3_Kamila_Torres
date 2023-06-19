let count = 0;
const btn = document.getElementById('btn');
btn.addEventListener('click', () => {
  fetch('https://api.escuelajs.co/api/v1/users')
    .then(response => response.json())
    .then(data => {
      const user = data.results[count];
      const name = `${user.name.first} ${user.name.last}`;
      const nameElement = document.getElementById('name');
      nameElement.textContent = name;
      count = (count + 1) % data.results.length;
    })
    .catch(error => console.log(error));
});
