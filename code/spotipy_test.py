import sys
import spotipy
import spotipy.util as util
import urllib.request



if __name__ == '__main__':
    #check that command line input has a Spotify username
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    #prompt API for tokens
    token = util.prompt_for_user_token(username)

    #check token validity
    if token:
        #create our spotipy object to begin importing
        sp = spotipy.Spotify(auth=token)
        track_to_analyze = sp.audio_features("spotify:track:1i6N76fftMZhijOzFQ5ZtL") #should be removed for final
        #import playlist

        #iterate through classifier playlist (make sure to know how decades are segmented and do them separately)
            #for each song, gather spotify features, and download song for audio analysis learned in class

        #make classifier from features

        #iterate through testing playlist
            #for each song, gather all the features in previous for loop and classify

        #show results

        print(sp.track("spotify:track:1i6N76fftMZhijOzFQ5ZtL")['preview_url']) #should be removed for final
        #downloads 30 second clip of requested file at local path
        urllib.request.urlretrieve(sp.track("spotify:track:1i6N76fftMZhijOzFQ5ZtL")['preview_url'], 'C:/Users/camer/Downloads/test2') #should be removed for final


    else:
        print("Can't get token for", username)