import json

import requests

from secrets import spotify_token, spotify_user_id


class CreatePlaylist:

    def create_playlist():
        #Create new playlist
        request_body = json.dumps({
            "name": "The Api Playlist",
            "description": "Added by Python",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/4wHIqfOQOiNdgZpa2J5K0W/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        #print(response_json['id'])
        #print(response_json)

    create_playlist()

    def add_songs():
        query = "https://api.spotify.com/v1/playlists/2DAHxvfahpTJex0AzHtWM8/tracks".format(spotify_token)
        request_body = json.dumps({
            "uris": ["spotify:track:6WrI0LAC5M1Rw2MnX2ZvEg"], "position": 1
        })
        response = requests.post(
            query,
            data=request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
        }
        )
        response_json = response.json()

        # print(response_json['id'])
        # print(response_json)
    add_songs()

    def add_cover():
        query = "https://api.spotify.com/v1/playlists/2DAHxvfahpTJex0AzHtWM8/images".format(spotify_token)

        request_body = json.dumps({
            "uris": ['spotify:playlist:2DAHxvfahpTJex0AzHtWM8'],
            "url": 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Dogs_like_cucumbers_%26_cucumbers_like_dogs.jpg/1024px-Dogs_like_cucumbers_%26_cucumbers_like_dogs.jpg',
            "height": 640,
            "width": 640
        })
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "image/jpeg",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # print(response_json['id'])
        # print(response_json)

    add_cover()



