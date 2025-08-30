def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    text = text.lower()
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_char_counts(char_counts):
    # keep only alphabetical characters, then sort by frequency (desc)
    items = [{"char": ch, "num": n} for ch, n in char_counts.items() if ch.isalpha()]
    items.sort(key=lambda x: x["num"], reverse=True)
    return items
