import requests
from tqdm import tqdm
import urllib.request
import os
import argparse

headers= {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36', 
        'Accept-Language': 'en-US,en;q=0.8'
}

def main(args):
    image_urls = []
    output_dir = args.output
    if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    url = "https://api.opensea.io/api/v1/assets"
    n = (args.iterations // 50) + 1

    pbar = tqdm(total=args.iterations)
    for i in range(0, n):
        querystring = {"order_direction":"asc",
                    "offset":i*50,
                    "order_by":"pk",
                    "collection":args.collection,
                    "limit":"50"}
        response = requests.request("GET", url, params=querystring)
        if response.status_code != 200:
            print('OpenSea API request error')
            break
        
        #Getting meebits data
        data = response.json()['assets']
        for image in data:
            pbar.update(1)
            image_urls.append(image['image_original_url'])
        
    pbar.close()
        


    with open(f"{args.collection}.txt", "w") as output:
            for row in image_urls:
                output.write(str(row) + '\n')

    for i, url in enumerate(tqdm(image_urls)):
        request_= urllib.request.Request(url,None,headers) 
        response = urllib.request.urlopen(request_)
        image = response.read()
        with open(f"{output_dir}/{i:04d}.png", "wb") as file:
                file.write(image)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-o", "--output", help="Output directory", default="output")
    parser.add_argument("-c", "--collection", help="Collection name", required=True)
    parser.add_argument("-i", "--iterations", help="Number of images to scrape", type=int, default=10000)

    
    # Read arguments from command line
    args = parser.parse_args()

    # calling the main function
    main(args)