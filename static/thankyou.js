window.onload = () => {
  const reviews = JSON.parse(localStorage.getItem("reviews"));
  const summary = reviews.length ? reviews[0].summary : "";

  const results = reviews.map(
    (review) =>
      `<li class="list-group-item">
        <h5>${review.title} - ${review.rating} stars</h5>
        <p>${review.text}</p>
        <small>Date: ${review.date}</small>
      </li>`
  );

  document.getElementById("results").innerHTML = `<ul class="list-group">${results.join("")}</ul>`;
  document.getElementById("summaries").innerHTML = `<div class="card my-4"><div class="card-body">${summary}</div></div>`;
};
