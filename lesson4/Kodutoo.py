def search(word, text):
    if word in text:
        word_index = text.index(word)
        sub_text = text[word_index - 10 : word_index + 10 + len(word)]
        return sub_text
    else:
        return "Not word in this text"





if __name__ == '__main__':
    # Maritime-related string (Length between 100 and 200 characters)
    maritime_text = """
    The vast ocean is the lifeblood of global trade, with ships navigating the seas, transporting goods across continents. Mariners brave the unpredictable waters, relying on advanced navigational instruments, weather forecasting, and their own skill to ensure the safety of both vessel and crew.
    """
    
   # Example: Getting a substring by index
    start_index = 10  # Starting index for the substring
    end_index = 80  # Ending index for the substring

    # Extract the substring using Python slicing
    substring = maritime_text[start_index:end_index]

    # Print the full text and the extracted substring
    # print("Full Maritime Text:")
    # print(maritime_text)
    # print("Extracted Substring (from index 10 to 80):")
    # print(substring)

    print(search("goods", maritime_text))




