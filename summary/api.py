def get_summary(file_content):
    # This function mocks the actual call to the OpenAI GPT Chat API
    # In a real implementation, you would use the API key to authenticate and make the API call
    summary = f"Summary of the file: (mocked)\n\n{file_content[:100]}..."
    return summary
