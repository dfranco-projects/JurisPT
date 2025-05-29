import re
import unicodedata

class Cleaner:
    def __init__(self) -> None:
        pass

    def remove_accents(self, text: str) -> str:
        """
        Removes accents from the text.

        Args:
            text (str): input text.

        Returns:
            str: text without accents.
        """
        return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

    def clean(self, text: str) -> str:
        """
        Cleans and normalizes raw legal text.

        Args:
            text (str): raw input text.

        Returns:
            str: cleaned and normalized text.
        """
        # normalize unicode and remove accents
        text = self.remove_accents(text)

        # normalize line endings
        text = text.replace('\r\n', '\n').replace('\r', '\n')

        # remove excessive blank lines
        text = re.sub(r'\n\s*\n+', '\n\n', text)

        # strip leading/trailing whitespace from each line
        text = '\n'.join(line.strip() for line in text.splitlines())

        # remove multiple spaces
        text = re.sub(r'[ \t]+', ' ', text)

        # lowercase
        text = text.lower()

        return text.strip()