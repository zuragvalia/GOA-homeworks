def manual_replace(text, old, new):
    if old in text:
        text = text.replace(old, new)
    return text
