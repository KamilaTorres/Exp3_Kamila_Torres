let currentImageUrl = '';

function fetchRandomDog() {
  fetch("https://random.dog/woof.json")
    .then(response => response.json())
    .then(data => {
      const dogImageContainer = document.getElementById("dog-image-container");
      const imageUrl = data.url;

      if (imageUrl === currentImageUrl) {
        // Si la imagen actual es la misma que la anterior, volvemos a llamar a la API para obtener una nueva
        fetchRandomDog();
        return;
    }

      currentImageUrl = imageUrl;
      dogImageContainer.innerHTML = '';

      if (imageUrl.endsWith(".mp4")) {
        // Si la URL es un video, volvemos a llamar a la API para obtener una nueva imagen
        fetchRandomDog();
        return;
    }
      else {
        // Si la URL es una imagen, crea un elemento de imagen
        const imageElement = document.createElement("img");
        imageElement.src = imageUrl;
        imageElement.classList.add("dog-image");
        dogImageContainer.appendChild(imageElement);
    }
      
    })
    .catch(error => {
      console.error("Error al obtener los datos de la API:", error);
    });
}

document.getElementById("next-button").addEventListener("click", fetchRandomDog);

// Cargar la primera imagen al cargar la página
fetchRandomDog();
