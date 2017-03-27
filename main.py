'''
Main Script that downloads a Youtube video from the path fiven as argument
'''

import os
import youtube_dl
import fire

# Build a directory where to save the downloaded videos
if not os.path.exists('download/'):
	os.makedirs('download/')

class Downloader(object):

	def __init__(self):
		'''
		Initializes the downloader for youtube videos
		'''
		self.options = {
			# 'format': 'bestaudio/best', # choice of quality
			# 'extractaudio' : True,      # only keep the audio
			# 'audioformat' : "mp3",      # convert to mp3 
			'outtmpl': 'download/%(id)s.mp4',        # name the file the ID of the video
			# 'noplaylist' : True,}       # only download single song, not playlist
			}
		self.ydl = youtube_dl.YoutubeDL(self.options)

	def download(self, url):
		'''
		Downloads the Youtube video at that url and returns information
		on the download
		url -- string
			url of the video to download
		'''
		# Downloads the video
		r = self.ydl.extract_info(url, download=True)
		save_path = os.path.join('download/', '%s.mp4' % r['title'])
		os.rename('download/%s.mp4'%r['id'], save_path)

		# print some typical fields on the downloaded video
		str  = "%s was uploaded by '%s' and has %d views, %d likes, and %d dislikes"
		print str % (r['title'], r['uploader'], r['view_count'], r['like_count'], r['dislike_count'])

		
if __name__ == '__main__':
	# url = "https://youtu.be/dMK_npDG12Q"
	fire.Fire(Downloader)
	