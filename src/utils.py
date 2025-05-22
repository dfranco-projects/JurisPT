import re

def normalize_filename(filename: str) -> str:
    """
    Converts a law_id string into a clean, lowercase filename with .txt extension.
    e.g., "Decreto-Lei n.º 90-C/2022" becomes "decreto_lei_n_90_c_2022.txt".
    
    Args:
        filename (str): The original law_id string to normalize.
    
    Returns:
        str: A sanitized, underscore-delimited filename ending in .txt.
    """
    # lowercase
    filename = filename.lower()

    # split on spaces or slashes or hyphen and join with underscores
    parts = re.split(r'[ /-]+', filename)
    filename = '_'.join(parts)

    # remove any remaining non-alphanumeric or underscore characters
    filename = re.sub(r'[^a-z0-9_]', '', filename)

    # add .txt extension
    return filename + '.txt'