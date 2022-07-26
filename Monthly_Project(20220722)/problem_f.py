# 영화의 순수익(revenue - budget)을 따져보자!
# 순수익 1등 영화는 무엇일까?
import json


def dec_movies(movies):
    movie_dict = []  # 영화 id, 제목 저장 이중 리스트
    film_list = []  # 영화 제목 리스트
    revenue_list = []   # 수익 리스트
    budget_list = []    # 예산 리스트
    answer = 0
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_dict.append({id: title})
        film_json = open(f'data/movies/{id}.json', encoding='utf-8')
        film_dict = json.load(film_json)
        revenue_list.append(film_dict.get('revenue'))
        budget_list.append(film_dict.get('budget'))
    profit = 0
    for m in range(len(budget_list)):
        true_revenue = revenue_list[m] - budget_list[m]
        if answer < true_revenue:
            answer = true_revenue
            profit = m
    for val in movie_dict[profit].values():
        return val


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
