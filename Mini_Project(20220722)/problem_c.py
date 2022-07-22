import json
from pprint import pprint


def movie_info(movies, genres):
    del_category = [
        'popularity', 'release_date', 'video',
        'original_language', 'original_title',
        'adult', 'backdrop_path', 'vote_count'
    ]
    for movie in movies:
        for i in del_category:
            del(movie[i])
        genres_add = []
        for genre_num in movie['genre_ids']:
            for genre_dic in genres:
                if genre_dic.get('id') == genre_num:
                    genres_add.append(genre_dic.get('name'))
        movie['genres'] = genres_add
        del(movie['genre_ids'])

    return movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
