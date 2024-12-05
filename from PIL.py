from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_geolocation(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    
    if exif_data is not None:
        for tag, value in exif_data.items():
            if TAGS.get(tag) == 'GPSInfo':
                gps_info = value
                return gps_info
    return None

image_path = "your_image.jpg"
gps_data = get_geolocation(image_path)
if gps_data:
    print("GPS Data:", gps_data)
else:
    print("No GPS data found.")