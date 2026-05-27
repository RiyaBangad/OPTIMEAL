def detect_category(text):
    text = text.lower()

    if "chips" in text or "snack" in text:
        return "Snack 🍟"

    elif "juice" in text or "drink" in text or "cola" in text:
        return "Beverage 🥤"

    elif "milk" in text or "cheese" in text:
        return "Dairy 🥛"

    elif "chocolate" in text or "cake" in text:
        return "Junk Food 🍩"

    else:
        return "General Food 🍽️"