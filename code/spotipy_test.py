import sys
import spotipy
import spotipy.util as util



if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        track_to_analyze = sp.audio_analysis("spotify:track:1i6N76fftMZhijOzFQ5ZtL")
        print(track_to_analyze['sections'])
    else:
        print("Can't get token for", username)