from transformers import pipeline

def summarize_text(text, max_len=150, min_len=40):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    sample_text = """Your long input text here..."""
    print("Summary:")
    print(summarize_text(sample_text))
