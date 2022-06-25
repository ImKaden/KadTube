from kadparser import *

class Visual:
	def __init__(self):
		self.channel_list = []
		self.video_list = []

	def query_request(self):
		return input("---> ")

	def channels(self, query):
		channel = Channel(query)

		for channel_id, channel in enumerate(channel.search()):
			self.channel_list.append(f"{channel_id + 1}. | {channel['name']} ---> {channel['subscribers']} subs")

		return self.channel_list

	def videos(self, query):
		video = Video(query)

		for video_id, video in enumerate(video.search()):
			self.video_list.append(f"{video_id + 1}. | {video['title']} [{video['channel']}] ---> {video['views']}")

		return self.video_list

visual = Visual()