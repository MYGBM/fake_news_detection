import re


class Normalize:
    def __init__(self) -> None:
        self.normalization_rules = [
            (r"[ሐሃኻሓኀኃ]", "ሀ"),
            (r"[ሑኁኹ]", "ሁ"),
            (r"[ሒኂኺ]", "ሂ"),
            (r"[ሔኄኼ]", "ሄ"),
            (r"[ሕኅኽ]", "ህ"),
            (r"[ሖኆኾ]", "ሆ"),
            (r"[ኇ]", "ሗ"),
            (r"[ሠ]", "ሰ"),
            (r"[ሡ]", "ሱ"),
            (r"[ሢ]", "ሲ"),
            (r"[ሣ]", "ሳ"),
            (r"[ሤ]", "ሴ"),
            (r"[ሥ]", "ስ"),
            (r"[ሦ]", "ሶ"),
            (r"[ሧ]", "ሷ"),
            (r"[ኣዐዓ]", "አ"),
            (r"[ዑ]", "ኡ"),
            (r"[ዒ]", "ኢ"),
            (r"[ዔ]", "ኤ"),
            (r"[ዕ]", "እ"),
            (r"[ዖ]", "ኦ"),
            (r"[ጸ]", "ፀ"),
            (r"[ጹ]", "ፁ"),
            (r"[ጺ]", "ፂ"),
            (r"[ጻ]", "ፃ"),
            (r"[ጼ]", "ፄ"),
            (r"[ጽ]", "ፅ"),
            (r"[ጾ]", "ፆ"),
            (r"(ሉ[ዋአ])", "ሏ"),
            (r"(ሑ[ዋአ])", "ሗ"),
            (r"(ሙ[ዋአ])", "ሟ"),
            (r"(ቱ[ዋአ])", "ቷ"),
            (r"(ሩ[ዋአ])", "ሯ"),
            (r"(ሱ[ዋአ])", "ሷ"),
            (r"(ሹ[ዋአ])", "ሿ"),
            (r"(ቁ[ዋአ])", "ቋ"),
            (r"(ቡ[ዋአ])", "ቧ"),
            (r"(ቹ[ዋአ])", "ቿ"),
            (r"(ሁ[ዋአ])", "ኋ"),
            (r"(ኑ[ዋአ])", "ኗ"),
            (r"(ኙ[ዋአ])", "ኟ"),
            (r"(ኩ[ዋአ])", "ኳ"),
            (r"(ዙ[ዋአ])", "ዟ"),
            (r"(ጉ[ዋአ])", "ጓ"),
            (r"(ደ[ዋአ])", "ዷ"),
            (r"(ጡ[ዋአ])", "ጧ"),
            (r"(ጩ[ዋአ])", "ጯ"),
            (r"(ጹ[ዋአ])", "ጿ"),
            (r"(ፉ[ዋአ])", "ፏ"),
        ]

    def normalize_data(self, text: str) -> str:
    
        import re


        # # Step 1: Remove URLs
        # text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", text)
        # text = re.sub(r'<[^>]*>', '', text)
        # # Step 2: Remove English words and digits
        # text = re.sub(r"[a-zA-Z]|[0-9]+", " ", text)
        # # Step 3: Remove Amharic Geez numbers
        # text = re.sub(r"[፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻]", "", text)
        # # Step 4: Remove special characters and punctuation
        # text = re.sub(r"[^\w\s]|_|-", "", text)
        # text = re.sub(r'(.)\1+', r'\1\1', text)
        # # Step 5: Remove emojis
        # text = re.sub(r"[\U00010000-\U0010ffff]", " ", text)
        # # Step 6: Remove extra spaces and leading/trailing spaces
        # text = re.sub(r"\s+", " ", text.strip())

        text = re.sub(r"[^\w\s]|[_\uD800-\uDBFF\uDC00-\uDFFF-]", " ", text.strip())
        for pattern, replacement in self.normalization_rules:
            text = re.sub(pattern, replacement, text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()
