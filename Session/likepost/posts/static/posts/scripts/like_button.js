// like_button.js

const likeButton = document.getElementById('likeButton');

if (isLiked) {
  // Change the button's text and style when is_liked is true
  likeButton.textContent = 'Unlike';
  likeButton.classList.add('liked');

  // Add an event listener to toggle the like state when clicked
  likeButton.addEventListener('click', () => {
    // Send a request to the server to unlike the post
    fetch('{% url "unlike-post" %}', {
      method: 'POST',
      headers: { 'X-CSRFToken': '{{ csrf_token }}' },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Update the button's state after unliking
      likeButton.textContent = 'Like';
      likeButton.classList.remove('liked');
    })
    .catch(error => console.error(error));
  });
} else {
  // Add an event listener to toggle the like state when clicked
  likeButton.addEventListener('click', () => {
    // Send a request to the server to like the post
    fetch('{% url "like-post" %}', {
      method: 'POST',
      headers: { 'X-CSRFToken': '{{ csrf_token }}' },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      // Update the button's state after liking
      likeButton.textContent = 'Unlike';
      likeButton.classList.add('liked');
    })
    .catch(error => console.error(error));
  });
}
