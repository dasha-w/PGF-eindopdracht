#https://www.youtube.com/watch?v=97gUjB_t_ls&t=31s
import requests
import matplotlib.pyplot as plt
import matplotlib.image as myimg
from io import BytesIO

endpoints ='https://dog.ceo/api/breeds/image/random'

#'https://api.nationalize.io?name=nathaniel'
#payload = {'name': 'Dagmar'}
#'https://dog.ceo/api/breeds/image/random'

try:
    response = requests.get(endpoints) #, params = payload)
    if response.status_code == 200:
        data = response.json()
        #print(data)

        if data:
            img_url = data.get('message')
            #print(img_url)
            img_response = requests.get(img_url)
            img = myimg.imread(BytesIO(img_response.content), format = 'auto')
            plt.imshow(img)
            plt.show()

        else:
            print("No data available")

    else:
        print(f'Error {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error {e}')