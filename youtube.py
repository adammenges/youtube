import pafy
import os

# playlist_url = raw_input("What's the URL of the playlist? ")
# 
# playlist_url = "https://www.youtube.com/playlist?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9" # Hintons class
# playlist_url = "https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC" # Karpathy's class
# playlist_url = "https://www.youtube.com/playlist?list=PL7194650F2DD2AB07"                 # Game Theory: Yale University
# playlist_url = "https://www.youtube.com/playlist?list=PLGo75GaSHoJnrL5ccqsVOXtI52YLJVU5w" # Yoga
# playlist_url = "https://www.youtube.com/playlist?list=PLdk2fd27CQzT7opzoGHvqDuDbltozWn7O" # Spectral Clustering
# playlist_url = "https://www.youtube.com/playlist?list=PL7ddpXYvFXspUN0N-gObF1GXoCA-DA-7i" # Computational photography

playlist_url = "https://www.youtube.com/playlist?list=PLfYUBJiXbdtS2UQRzyrxmyVHoGW0gmLSM" # fast ai

def download_playlist(playlist):
	playlist = pafy.get_playlist(playlist_url)
	videos = playlist['items']
	directory = "./" + playlist['title']

	if not os.path.exists(directory):
		os.makedirs(directory)

	amount_ive_downloaded = 6

	for video in videos:
		p = video['pafy']
		best = p.getbest(preftype="mp4")
		title = best.title.replace('/', '--')
		print title
		filepath = directory + "/" + title + "." + best.extension
		best.download(filepath=filepath)

	print '\n\n'
	print "Done."

def download_video(video_url):
	video = pafy.new(video_url)
	print 'downloading -- ' + video.title
	best = video.getbest(preftype="mp4")
	directory = "."
	title = best.title.replace('/', '--')
	filepath = directory + "/" + title + "." + best.extension
	best.download(filepath=filepath)

download_playlist(playlist_url)
