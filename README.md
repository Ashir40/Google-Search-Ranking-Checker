Google Search Ranking Checker
This Python script checks the ranking of a given URL for a specific keyword in the Google search results. It uses the requests and BeautifulSoup libraries for web scraping to extract the URLs of the search results from the Google search page.

Function 1: get_google_results()
This function takes a query parameter, which is the keyword you want to search for in Google. It makes a GET request to the Google search page with the given keyword and returns a list of URLs that appear in the search results.

The function uses the requests library to make the GET request and the BeautifulSoup library to parse the HTML content of the search page. It looks for all the a tags on the page and extracts the href attribute of each tag. It then filters the URLs that start with /url?q= and extracts the actual URL from that string using the split() function.

Function 2: get_ranking()
This function takes two parameters: keyword and url. The keyword parameter is the keyword you want to search for in Google, and the url parameter is the URL you want to check the ranking for. It uses the get_google_results() function to get a list of URLs that appear in the search results for the given keyword. It then loops through the list of URLs and checks if the given URL is present in the list. If it is present, it returns the index of the URL in the list, incremented by 1, which represents the ranking of the URL in the search results. If the URL is not present in the list, the function returns -1, indicating that the URL is not ranked for the given keyword.

Example Usage
The example usage provided in the script shows how to use the get_ranking() function to check the ranking of a given URL for a specific keyword. You need to provide the keyword and URL values as parameters for the function. If the URL is ranked for the given keyword, the script will print the ranking position, and if it is not ranked, it will print a message indicating that the URL is not ranked for the given keyword.

Overall, this Python script provides a simple and effective way to check the ranking of a URL for a specific keyword in the Google search results, which can be useful for SEO professionals, digital marketers, and website owners who want to monitor their website's visibility on Google.
