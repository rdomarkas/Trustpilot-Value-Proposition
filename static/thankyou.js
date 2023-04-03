window.onload = () => {
  const reviews = JSON.parse(localStorage.getItem("reviews"));

  const results = reviews.map(
    (review) =>
      `<li class="list-group-item">
        <h5>${review.title} - ${review.rating} stars</h5>
        <p>${review.text}</p>
        <small>Date: ${review.date}</small>
      </li>`
  );

  const summaries = reviews.map(
    (review) => `<li class="list-group-item">${review.summary}</li>`
  );

  document.getElementById("results").innerHTML = `<ul class="list-group">${results.join("")}</ul>`;
  document.getElementById("summaries").innerHTML = `<ul class="list-group">${summaries.join("")}</ul>`;
};
