import re
import tiktoken

class Chunker:
    def __init__(self, max_tokens=512, overlap=50, encoding_name="cl100k_base") -> None:
        """
        Initializes the chunker.

        Args:
            max_tokens (int): maximum tokens per chunk.
            overlap (int): number of tokens to overlap between chunks.
            encoding_name (str): tokenizer encoding name.
        """
        self.max_tokens = max_tokens
        self.overlap = overlap
        self.enc = tiktoken.get_encoding(encoding_name)

    def chunk_by_legal_markers(self, text: str) -> list:
        """
        Splits text into chunks by legal markers (articles, sections, chapters).

        Args:
            text (str): cleaned input text.

        Returns:
            list: list of legal section/article chunks.
        """
        # regex for common Portuguese legal markers
        pattern = r'(?=^((artigo|cap[ií]tulo|sec[cç][aã]o|t[ií]tulo|livro|[IVXLCDM]+)\s*[0-9]*\.?º?))'

        # split, keeping markers at the start of each chunk
        chunks = re.split(pattern, text, flags=re.IGNORECASE | re.MULTILINE)

        # re-attach markers to their content
        merged = []
        i = 1
        while i < len(chunks):
            marker = chunks[i].strip()
            content = chunks[i+1].strip() if (i+1) < len(chunks) else ""
            merged.append(f"{marker} {content}".strip())
            i += 2

        # filter out empty chunks
        return [c for c in merged if c]

    def chunk_by_tokens(self, text: str) -> list:
        """
        Splits text into overlapping chunks by token count.

        Args:
            text (str): cleaned input text.

        Returns:
            list: list of token-based chunks.
        """
        # encode text into tokens
        tokens = self.enc.encode(text)
        chunks = []
        start = 0

        # iterate over tokens, creating overlapping chunks
        while start < len(tokens):
            end = min(start + self.max_tokens, len(tokens))

            # decode tokens back to text for this chunk
            chunk_tokens = tokens[start:end]
            chunk_text = self.enc.decode(chunk_tokens)
            chunks.append(chunk_text.strip())

            # if at the end, break
            if end == len(tokens):
                break

            # move start forward by max_tokens minus overlap
            start += self.max_tokens - self.overlap

        return chunks

    def chunk(self, text: str) -> list:
        """
        Main chunking function for laws with articles inside.
        Splits by legal markers (articles/sections), then further splits long articles by tokens.

        Args:
            text (str): cleaned input text.

        Returns:
            list: list of final chunks (each <= max_tokens).
        """
        final_chunks = []

        # first, split by legal markers (articles, sections, etc.)
        legal_chunks = self.chunk_by_legal_markers(text)

        for chunk in legal_chunks:
            # if chunk is too long, further split by tokens
            if len(self.enc.encode(chunk)) > self.max_tokens:
                token_chunks = self.chunk_by_tokens(chunk)
                final_chunks.extend(token_chunks)
            else:
                final_chunks.append(chunk.strip())

        # filter out empty chunks
        return [c for c in final_chunks if c]