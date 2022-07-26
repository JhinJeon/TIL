import json
from xml.dom import INDEX_SIZE_ERR


def max_revenue(movies):
    movie_list = []
    revenue_list = []
    answer = 0
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_list.append([id, title])
        revenue_json = open(f'data/movies/{id}.json', encoding='utf-8')
        revenue_dict = json.load(revenue_json)
        revenue_list.append(revenue_dict.get('revenue'))
    max_revenue = 0
    for m in range(len(revenue_list)):
        if revenue_list[m] > max_revenue:
            max_revenue = revenue_list[m]
            idx = m
    return movie_list[idx][1]

    # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))
