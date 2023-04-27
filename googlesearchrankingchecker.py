import requests    
from bs4 import BeautifulSoup

def get_google_results(query): #  This line starts the definition of the function named get_google_results that takes one argument called query.
    res = requests.get(f'https://www.google.com/search?q={query}') # This line sends an HTTP GET request to the Google search page with the provided query and stores the response in the res variable.
    soup = BeautifulSoup(res.text, 'html.parser') # This line creates a BeautifulSoup object soup to parse the HTML content of the response stored in the res variable.
    results = [] # This line creates an empty list called results to store the search results. 
    for i, link in enumerate(soup.find_all('a')): # This line starts a loop that iterates over each <a> tag in the parsed HTML using the find_all method of BeautifulSoup. The enumerate function is used to get both the index (i) and the value (link) of each iteration.
        href = link.get('href')  # This line extracts the value of the href attribute of the current <a> tag and stores it in the href variable.
        if href.startswith('/url?q='): # This line checks whether the href value starts with the string '/url?q='.
            href = href.split('/url?q=')[1].split('&')[0] # Split function split strings into sub strings
            results.append(href) # Add href into result string 
    return results 

def get_ranking(keyword, url): # Defining funtion that enters two arguments
    results = get_google_results(keyword) # It stores the return list of urls from get_google_function in results variable.
    for i, result in enumerate(results): # This line starts a loop that iterates over each URL in the results list using the enumerate function to get both the index (i) and the value (result) of each iteration.
        if url in result: # to see if URL is in the result
            return i + 1 # If the url argument is found in the result URL, this line returns the index i incremented by 1 (to convert from 0-based to 1-based ranking).
    return -1 # If the url argument is not found in any of the URLs in the results list, this line returns -1 to indicate that the website does not rank for the given keyword.

# Example usage
keyword = "Maxenius" # Type your keyword here inside the single inverted commas
url = 'https://maxenius.com/' # Enter the URL in the single inverted commas
ranking = get_ranking(keyword, url)
if ranking == -1:
    print(f'The Website "{url}" \nDoes not rank for the keyword "{keyword}"')
else:
    print(f'The website "{url}" \nRanks #{ranking} for the keyword "{keyword}"')




















