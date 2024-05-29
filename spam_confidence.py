def compute_average_spam_confidence(filename):
    """
    This function processes a file to find X-DSPAM-Confidence lines,
    extracts the confidence values, and calculates the average.

    Args:
        filename: The name of the file to process.

    Returns:
        The average spam confidence as a float, or None if no lines were found.
    """

    count = 0
    total = 0.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    # Find the position of the colon and extract the number
                    colon_pos = line.find(':')
                    confidence_str = line[colon_pos + 1:].strip()  # Strip to remove surrounding whitespace
                    try:
                        confidence = float(confidence_str)
                        count += 1
                        total += confidence
                    except ValueError:
                        pass  # Ignore lines with non-numeric confidence values
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

    if count > 0:
        average = total / count
        print("Average spam confidence:", average)
    else:
        print("No X-DSPAM-Confidence lines found")
        return None

    return average

if __name__ == "__main__":
    filename = input("Enter a file name: ")
    compute_average_spam_confidence(filename)
