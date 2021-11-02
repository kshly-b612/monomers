import re
import urllib.parse
import urllib.request

def youtube(search: str):
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen(f"https://www.youtube.com/results?{query_string}")
    search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
    for index in range(0, 10):
        print(f"{index + 1}. https://www.youtube.com/watch?v={search_results[index]}")
youtube(input("query: "))
