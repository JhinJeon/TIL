import json


def dec_movies(movies):
    movie_list = []
    date_list = []
    recommend_list = []
    answer = 0
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movie_list.append([id, title])
        date_json = open(f'data/movies/{id}.json', encoding='utf-8')
        date_dict = json.load(date_json)
        date_list.append(date_dict.get('release_date'))
    max_revenue = 0
    for m in range(len(date_list)):
        if date_list[m][5:7] == '12':
            recommend_list.append(movie_list[m][1])
    return recommend_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(dec_movies(movies_list))
