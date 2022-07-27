import json
from pprint import pprint


def movie_info(movie):
    movie_info = {
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview')
    }
    return movie_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)

    pprint(movie_info(movie_dict))