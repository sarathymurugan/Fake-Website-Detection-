import requests
import validators

# Function to check if URL is valid
def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        print("Invalid URL")
        return False

# Function to check if the URL has HTTPS
def check_https(url):
    if url.startswith("https://"):
        return True
    else:
        print("No HTTPS detected. This may be insecure.")
        return False

# Function to check for suspicious keywords
def check_suspicious_keywords(url):
    suspicious_keywords = ['login', 'secure', 'paypal', 'account', 'update']
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            print(f"Suspicious keyword detected: {keyword}")
            return True
    return False

# Main function to analyze the URL
def analyze_url(url):
    if not is_valid_url(url):
        return "Invalid URL format."

    print(f"Analyzing: {url}")
    
    if not check_https(url):
        return "Warning: No HTTPS detected."
    
    if check_suspicious_keywords(url):
        return "Warning: Suspicious keywords detected."
    
    return "The website seems safe."

# Allow user input and execute analysis
if __name__ == "__main__":
    user_url = input("Enter the URL to analyze: ")
    result = analyze_url(user_url)
    print(result)
