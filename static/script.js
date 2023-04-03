document.getElementById("scraper-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const url = document.getElementById("url").value;
  const numPages = document.getElementById("num-pages").value;
  const starRating = document.getElementById("star-rating").value;
  const summaryPrompt = document.getElementById("summary-prompt").value;

  const data = {
    url: url,
    num_pages: numPages,
    star_rating: starRating,
    summary_prompt: summaryPrompt,
  };

  try {
    const response = await fetch("/scrape_reviews", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const reviews = await response.json();
      localStorage.setItem("reviews", JSON.stringify(reviews));
      window.location.href = "/thankyou";
    } else {
      throw new Error("Failed to fetch reviews");
    }
  } catch (error) {
    console.error(error);
  }
});
