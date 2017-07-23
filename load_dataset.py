import requests
import shutil

breeds_url = 'https://dog.ceo/api/breeds/list' 
image_template = 'https://dog.ceo/api/breed/{}/images'

def download():
    r = requests.get(breeds_url)
    breed_list = r.json()['message']
    counter = 0
    for breed in breed_list:
        print("downloading breed {}".format(breed))
        breed_url = image_template.format(breed)
        r = requests.get(breed_url)
        dog_image_list = r.json()['message']
        for i, dog_url in enumerate(dog_image_list):
            counter += 1
            dog_response = requests.get(dog_url, stream=True)
            dog_response.raw.decode_content = True
            with open("images/{}_{}.jpg".format(breed, i), "wb") as f:
                shutil.copyfileobj(dog_response.raw, f)
    print("downloaded {} images".format(counter))

def main():
    download()

if __name__ == "__main__":
    main()
