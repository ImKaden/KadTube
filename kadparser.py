import requests	

from bs4 import BeautifulSoup

class Video:
	def __init__(self, url):
		self.__response = requests.get(url)
		self.__html = BeautifulSoup(self.__response.content, "lxml")
		self.__video_list = []

	def search(self):
		self.videos = self.__html.find_all("div", class_="pure-u-1 pure-u-md-1-4")

		for video in self.videos:
			video_data = video.find_all("p", class_="video-data")
			video_links = video.find_all("a")

			self.__video_list.append({
				"title": video.find("p", attrs={"dir": "auto"}).text,
				"link": "https://yewtu.be" + video_links[0]["href"],
				"thumbnail": "https://yewtu.be" + video.find("img", class_="thumbnail").get("src"),
				"shared": video_data[0].text,
				"views": video_data[1].text,
				"channel": video.find("p", class_="channel-name").text.replace("\xa0", " ✔"),
				"channel_link": "https://yewtu.be" + video_links[1]["href"]
			})

		return self.__video_list

class Channel:
	def __init__(self, query):
		self.__response = requests.get(f"https://yewtu.be/search?q={query}&type=channel")
		self.__html = BeautifulSoup(self.__response.content, "lxml")
		self.__channel_list = []

	def search(self):
		self.channels = self.__html.find_all("div", class_="pure-u-1 pure-u-md-1-4")

		for channel in self.channels:
			channel_data = channel.find_all("p")
			self.__channel_list.append({
				"name": channel_data[0].text.replace("\xa0", " ✔"),
				"link": "https://yewtu.be" + channel.find("a")["href"],
				"avatar": "https://yewtu.be" + channel.find("img").get("src"),
				"subscribers": channel_data[1].text.split()[0]
			})

		return self.__channel_list

	def videos(self):
		video = Video(self.__channel_list[0]["link"])
		return video.search()