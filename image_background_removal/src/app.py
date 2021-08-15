from rembg.bg import remove
import numpy as np
import io
from PIL import Image
# import sys

# # Adding parent's path
# sys.path.append('../../')

input_path = 'handbag.png'
output_path = 'out.png'

f = np.fromfile(input_path)
result = remove(f)
img = Image.open(io.BytesIO(result)).convert("RGBA")
img.save(output_path)