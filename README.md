# Opensea Image Scraper
A script to scrape and download image assets from OpenSea collections

## Usage
The following script wil download `number_of_images` images from the `colllection_name` collection (sorted by token id) and save it inside  the `output_dir`. Additionally, it will also save the list of image urls in `collection_name.txt`.
```
python scrape.py -o output_dir -c collection_name -i number_of_images
```

For exampe, if you want to download all 10k Bored Ape Yacht Club images.
```
python scrape.py -o D:/bored_apes -c boredapeyachtclub -i 10000
```

## License
This project is under license from MIT. For more details, see the LICENSE file.


