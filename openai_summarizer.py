import openai

# Replace 'your_api_key_here' with your actual OpenAI API key
openai.api_key = "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"

def summarize_reviews(reviews, prompt):
    review_texts = "\n".join([f"{i + 1}. {review['text']}" for i, review in enumerate(reviews)])
    
    full_prompt = f"{prompt}\n\nReviews:\n{review_texts}\n\nSummary:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=full_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    summary = response.choices[0].text.strip()
    return summary
