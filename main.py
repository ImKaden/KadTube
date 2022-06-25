from visual import visual

if __name__ == "__main__":
	query = visual.query_request()

	if "/channel" in query:
		for channel in visual.channels(query[9:]):
			print(channel)
	elif "/video" in query:
		for video in visual.videos(f"https://yewtu.be/search?q={query[7:]}&type=video"):
			print(video)
	else:
		print("[ERROR]: Invalid Syntax, check [h]elp.")