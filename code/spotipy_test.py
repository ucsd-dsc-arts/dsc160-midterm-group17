import sys
import spotipy
import spotipy.util as util
import urllib.request



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
        track_to_analyze = sp.audio_features("spotify:track:1i6N76fftMZhijOzFQ5ZtL")
        #track_sections = track_to_analyze['sections']
        #song_tempos = []
        #song_keys = []
        #song_time_signature = []
        #song_loudness = []
        #for s in track_sections:
        #    song_tempos.append(s["tempo"])
        #    song_time_signature.append(s["time_signature"])
        #    song_loudness.append(s["loudness"])

        print(sp.track("spotify:track:1i6N76fftMZhijOzFQ5ZtL")['preview_url'])
        #downloads 30 second clip of requested file at local path
        urllib.request.urlretrieve(sp.track("spotify:track:1i6N76fftMZhijOzFQ5ZtL")['preview_url'], 'C:/Users/camer/Downloads/test2')


    else:
        print("Can't get token for", username)