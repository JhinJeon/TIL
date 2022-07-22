import json
from pprint import pprint


def movie_info(movie, genres):
    movie_info = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genres': movie.get('genre_ids')
    }
    genres_add = []
    for i in genres:
        for j in range(len(movie_info['genres'])):
            if i.get('id') == movie_info['genres'][j]:
                genres_add.append(i.get('name'))
    movie_info['genres'] = genres_add
    return movie_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
