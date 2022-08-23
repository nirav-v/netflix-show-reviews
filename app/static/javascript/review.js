async function reviewFormHandler(event) {
  event.preventDefault();

  const reviewRating = document.querySelector("#stars").value.trim();
  const reviewText = document
    .querySelector('textarea[name="review-body"]')
    .value.trim();
  const movie_id = window.location.toString().split("/")[
    window.location.toString().split("/").length - 1
  ];

  if (reviewText) {
    const response = await fetch("/api/reviews", {
      method: "POST",
      body: JSON.stringify({
        movie_id,
        reviewText,
        reviewRating,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
}

document
  .querySelector(".review-form")
  .addEventListener("submit", reviewFormHandler);
