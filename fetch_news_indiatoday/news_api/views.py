from django.http import JsonResponse
from lxml import html
import requests

# Create your views here.

data = {'news': []}
#   Dictionary so that to save the input in json format, it is made global for further use.


def test(request):
    """
    Fetches and returns the news from front page in json format
    """
    r = requests.get('https://www.indiatoday.in/technology/news')

    tree = html.fromstring(r.content)

    img_src = tree.xpath('/html/body/div[1]/main/div/section/div[3]/div[1]/div/div/img/@src')
    headings = tree.xpath('/html/body/div[1]/main/div/section/div[3]/div[1]/div/div/h3/@title')
    content = tree.xpath('/html/body/div[1]/main/div/section/div[3]/div[1]/div/div/p/text()')

    for i in range(len(headings)):
        data['news'].append({
            'heading': headings[i],
            'content': content[i],
            'img_src': img_src[i]
        })

    return JsonResponse(data)

