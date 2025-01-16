
import re
class Preprocess:
    def __init__(self) -> None:
        self.normalization_rules = [
            (re.compile(r"[ሐሃኻሓኀኃ]"), "ሀ"),
            (re.compile(r"[ሑኁኹ]"), "ሁ"),
            (re.compile(r"[ሒኂኺ]"), "ሂ"),
            (re.compile(r"[ሔኄኼ]"), "ሄ"),
            (re.compile(r"[ሕኅኽ]"), "ህ"),
            (re.compile(r"[ሖኆኾ]"), "ሆ"),
            (re.compile(r"[ኇ]"), "ሗ"),
            (re.compile(r"[ሠ]"), "ሰ"),
            (re.compile(r"[ሡ]"), "ሱ"),
            (re.compile(r"[ሢ]"), "ሲ"),
            (re.compile(r"[ሣ]"), "ሳ"),
            (re.compile(r"[ሤ]"), "ሴ"),
            (re.compile(r"[ሥ]"), "ስ"),
            (re.compile(r"[ሦ]"), "ሶ"),
            (re.compile(r"[ሧ]"), "ሷ"),
            (re.compile(r"[ኣዐዓ]"), "አ"),
            (re.compile(r"[ዑ]"), "ኡ"),
            (re.compile(r"[ዒ]"), "ኢ"),
            (re.compile(r"[ዔ]"), "ኤ"),
            (re.compile(r"[ዕ]"), "እ"),
            (re.compile(r"[ዖ]"), "ኦ"),
            (re.compile(r"[ጸ]"), "ፀ"),
            (re.compile(r"[ጹ]"), "ፁ"),
            (re.compile(r"[ጺ]"), "ፂ"),
            (re.compile(r"[ጻ]"), "ፃ"),
            (re.compile(r"[ጼ]"), "ፄ"),
            (re.compile(r"[ጽ]"), "ፅ"),
            (re.compile(r"[ጾ]"), "ፆ"),
            (re.compile(r"(ሉ[ዋአ])"), "ሏ"),
            (re.compile(r"(ሑ[ዋአ])"), "ሗ"),
            (re.compile(r"(ሙ[ዋአ])"), "ሟ"),
            (re.compile(r"(ቱ[ዋአ])"), "ቷ"),
            (re.compile(r"(ሩ[ዋአ])"), "ሯ"),
            (re.compile(r"(ሱ[ዋአ])"), "ሷ"),
            (re.compile(r"(ሹ[ዋአ])"), "ሿ"),
            (re.compile(r"(ቁ[ዋአ])"), "ቋ"),
            (re.compile(r"(ቡ[ዋአ])"), "ቧ"),
            (re.compile(r"(ቹ[ዋአ])"), "ቿ"),
            (re.compile(r"(ሁ[ዋአ])"), "ኋ"),
            (re.compile(r"(ኑ[ዋአ])"), "ኗ"),
            (re.compile(r"(ኙ[ዋአ])"), "ኟ"),
            (re.compile(r"(ኩ[ዋአ])"), "ኳ"),
            (re.compile(r"(ዙ[ዋአ])"), "ዟ"),
            (re.compile(r"(ጉ[ዋአ])"), "ጓ"),
            (re.compile(r"(ደ[ዋአ])"), "ዷ"),
            (re.compile(r"(ጡ[ዋአ])"), "ጧ"),
            (re.compile(r"(ጩ[ዋአ])"), "ጯ"),
            (re.compile(r"(ጹ[ዋአ])"), "ጿ"),
            (re.compile(r"(ፉ[ዋአ])"), "ፏ"),
        ]
    

    def data_profile(self, dataframe, column_name: str) -> dict:  
        # Key checks
        checks = {
            "URLs": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            "English words/digits": r"[a-zA-Z]|[0-9]+",
            "Amharic Geez numbers": r"[፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻]",
            "Special characters/punctuation": r"[^\w\s]",
            "Emojis": r"[\U00010000-\U0010ffff]",
            "Extra spaces": r"\s{2,}",
            "HTML tags": r"<[^>]*>",
            "Elongated words": r"(.)\1{2,}",
        }
        
        # Dictionary to accumulate counts
        total_counts = {key: 0 for key in checks}
        total_counts["Leading/trailing spaces"] = 0
        # Iterate over each row in the specified column
        for text in dataframe[column_name]:
            # Convert text to string (handles NaN or non-string data)
            text = str(text)     
            for key, pattern in checks.items():
                matches = re.findall(pattern, text)
                total_counts[key] += len(matches)  # Add the count of matches for this row
            
            # Check leading/trailing spaces
            stripped_text = text.strip()
            if stripped_text != text:
                total_counts["Leading/trailing spaces"] += 1
    

        return total_counts


    def preprocess_data(self, text: str) -> str:
        text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", text)
        # Remove html tags
        text = re.sub(r'<[^>]*>', '', text)
        # Remove English words and digits
        text = re.sub(r"[a-zA-Z]|[0-9]+", "", text)
        # Remove Amharic Geez numbers
        text = re.sub(r"[፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻]", "", text)
        # Remove special characters and punctuation
        text = re.sub(r"[^\w\s]|_|-", "", text)
        # Remove emojis, and bold/italics, etc extra style texts which are neither special characters or english letters  like 𝗢𝗿𝗼𝗺𝗼𝗣𝗿𝗼𝘁𝗲𝘀𝘁𝘀𝗯𝗼𝗹𝗱𝑖𝑡𝑎𝑙𝑖𝑐
        text = re.sub(r"[\U00010000-\U0010ffff]", "", text)
        # Remove elongated words (2+ occurrences)
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)
        # Remove extra spaces and leading/trailing spaces
        text = re.sub(r"\s{2,}", " ", text)
        for pattern, replacement in self.normalization_rules:
            text = pattern.sub(replacement, text)
        return text.strip()
