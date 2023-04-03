import openai

openai.api_key = "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"

def summarize_review(text, prompt="Please summarize the following review:", model="text-davinci-002", max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=f"{prompt} {text}",
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    return summary
