import openai
from tiktoken import get_encoding
from typing import List

from .config import get_api_key
from .print_utils import print_colored

openai.api_key = get_api_key()

MAX_TOKENS = 4096  # Maximum tokens for OpenAI's GPT-4 model
ENCODING = get_encoding("cl100k_base")  # Encoding for GPT-4 model


def count_tokens(text: str) -> int:
    try:
        tokens = ENCODING.encode(text)
        return len(tokens)
    except Exception:
        return 0


def chunk_text(text: str, max_tokens: int) -> List[str]:
    words = text.split()
    chunks = []
    current_chunk = []
    current_chunk_size = 0

    for word in words:
        word_token_len = count_tokens(word) + 1  # Adding 1 for the space character

        if current_chunk_size + word_token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_chunk_size = word_token_len
        else:
            current_chunk.append(word)
            current_chunk_size += word_token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def get_summary(file_content: str) -> str:
    print_colored("Starting summary generation...", level="info")

    # Check if file_content exceeds maximum context length
    num_tokens = count_tokens(file_content)
    if num_tokens > MAX_TOKENS:
        print_colored(
            f"Input file exceeds maximum context length of {MAX_TOKENS} tokens.",
            level="error",
        )
        return ""

    chunks = chunk_text(
        file_content, MAX_TOKENS - 100
    )  # Reserve tokens for the conversation

    conversation_history = [
        {"role": "system", "content": "You are a summarizing assistant."},
    ]

    for i, chunk in enumerate(chunks):
        print_colored(
            f"Processing chunk {i + 1} of {len(chunks)} (chunk size: {count_tokens(chunk)} tokens)",
            level="info",
        )

        conversation_history.append(
            {"role": "user", "content": f"Summarize the following text:\n\n{chunk}"}
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
        )
        conversation_history.append(
            {
                "role": "assistant",
                "content": response.choices[0].message.content.strip(),
            }
        )
        summary = conversation_history[-1]["content"]

    print_colored("Summary generation complete.", level="success")

    return summary
