from django.http import JsonResponse
from lxml import html
import requests
from .models import News


# Create your views here.


def test(request):
    """
    Fetches and returns the news from front page in json format
    """
    response = requests.get('https://www.indiatoday.in/technology/news')

    data = {'news': []}
    #   Dictionary so that to save the input in json format.

    if response:

        tree = html.fromstring(response.content)

        img_src = tree.xpath('/html/body/div[1]/main/div[1]/section/div[3]/div[1]/div/div/img/@src')
        headings = tree.xpath('/html/body/div[1]/main/div[1]/section/div[3]/div[1]/div/div[2]/h3/@title')
        content = tree.xpath('/html/body/div[1]/main/div/section/div[3]/div[1]/div/div/p/text()')

        for i in range(len(img_src)):

            data_exist = News.objects.filter(heading=headings[i])

            if not data_exist:
                data_save_obj = News.objects.create(heading=headings[i], content=content[i], img_src=img_src[i])
                data_save_obj.save()

            data['news'].append({
                'heading': headings[i],
                'content': content[i],
                'img_src': img_src[i],
            })

        return JsonResponse(data)

    else:

        data['news'].append({
            'error': 'There is no response from the request.get() method'
        })

        return JsonResponse(data)
