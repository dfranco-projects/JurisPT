import re
import json

def mark_law_as_revoked(laws_metadata, law_id) -> None:
    """
    Sets the 'active' field to False for the law with the given law_id in the metadata list.

    Args:
        laws_metadata (list): List of law metadata dicts.
        law_id (str): The law ID to mark as revoked.

    Returns:
        list: The updated laws_metadata list.
    """
    for law in laws_metadata:
        if law.get("law_id") == law_id:
            law["active"] = False
            break

    return laws_metadata

def normalize_law_filename(filename: str) -> str:
    """
    Converts a law_id string into a clean, lowercase filename.
    e.g., "Decreto-Lei n.º 90-C/2022" becomes "decreto_lei_n_90_c_2022".
    
    Args:
        filename (str): original law_id string to normalize.
    
    Returns:
        str:s clean, underscore-delimited filename with .txt extension.
    """
    # lowercase
    filename = filename.lower()

    # split on spaces or slashes or hyphen and join with underscores
    parts = re.split(r'[ /-]+', filename)
    filename = '_'.join(parts)

    # remove any remaining non-alphanumeric or underscore characters
    filename = re.sub(r'[^a-z0-9_]', '', filename)

    return filename