import os
import sys
import requests
from urllib.request import urlopen

import cv2
import numpy as np

if __name__ == "__main__":
    url_list_file = sys.argv[1]
    image_type = os.path.basename(os.path.splitext(url_list_file)[0])
    root_dir = sys.argv[2] # Directory of dataset to save to in as trainA
    start_idx = 0
    if len(sys.argv) > 3:
        start_idx = int(sys.argv[3])

    dataset_dir = os.path.join(root_dir, 'trainA')
    os.makedirs(dataset_dir, exist_ok=True)
    with open(url_list_file, encoding='utf-8') as url_list:
        for i, url in enumerate(url_list.readlines()):
            if i < start_idx:
                continue
            url = url.strip()
            print(url)
            newfile = os.path.join(dataset_dir, f'{image_type}_{i}.jpg')
            try:
                response = requests.get(url, timeout=5)
                if not response.ok:
                    continue
                with open(newfile, 'wb') as img:
                    img.write(response.content)
                # req = urlopen(url)
                # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                # img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
                img = cv2.imread(newfile)
                img = cv2.resize(img, (256,256))

                cv2.imwrite(newfile, img)
                print(newfile, ': success! ')
            except Exception as e:
                print(newfile, ': failure! ', e)
