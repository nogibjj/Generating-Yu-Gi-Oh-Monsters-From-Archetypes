import requests
import json 
import time
import os


# Draws the download progress bar for images
def draw_loader(file, total, count):
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Downloading images\n')
	print(file, end='')
	print(' ' + str(count) + ' of ' + str(total))
	percent = (count/total) * 100
	print('[', end='')
	for i in range(30):
		if (i/30) * 100 >= percent:
			print('-', end='')
		else:
			print('#', end='')
	print(']{:.2f}%'.format(percent))


# Receives the JSON and returns a list with the IDs and the links to the images
def prepare_json(data_request):
	data = json.loads(data_request)['data']
	link_images = []
	for i in range(len(data)):
		for j in range(len(data[i]['card_images'])):
			id = data[i]['card_images'][j]['id']
			link = data[i]['card_images'][j]['image_url']
			link_images.append([str(id), link])
	return link_images


def main():
	# Link to the API for over 11,000 cards
	url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
	request = requests.get(url)
	data_request = request.content

	# Prepares the links of the images
	link_images = prepare_json(data_request)
	image_quantity = len(link_images)

	# For each card, fetches all images and stores them in the dataset/ directory
	for i in range(image_quantity):
		id = link_images[i][0]
		link = link_images[i][1]
		file_name = id + '.jpg'

		# Draws progress bar 
		draw_loader(file_name, image_quantity, i+1)

		# Downloads the file
		image = requests.get(link, allow_redirects=True)
		open('dataset/' + file_name, 'wb').write(image.content)

		# Sleeps to not exceed the limit allowed by the API
		time.sleep(0.05)
	print('Process Finished!')


if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	main()
