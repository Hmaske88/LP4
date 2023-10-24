try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    import sys
    import os
    from geopy.geocoders import Nominatim
    import time
    import pyfiglet

except Exception:
    raise ModuleNotFoundError

def image():
    if os.path.exists("C:\\Users\\heman\\OneDrive\\Documents\\SEM 7\\LP4\\image"):
        for images in os.listdir("C:\\Users\\heman\\OneDrive\\Documents\\SEM 7\\LP4\\image"):
            if images.endswith(".jpg"):
                check_exif(images)
            else: 
                sys.exit("The image format should be JPG OR JPEG") 
                
def check_exif(picture): 
    pics = Image.open(f"C:\\Users\\heman\\OneDrive\\Documents\\SEM 7\\LP4\\image\\{picture}")
    img_exif = pics._getexif()
    
    for _ in range(0,1):
        if img_exif is None: 
            print("No EXIF in the picture!") 
            print("\n")
            continue
        else: 
            main(picture)
            
def convert_lat_long (degree: float, minutes: float, seconds: float): ## converting the longitude and latitude
    min = minutes / 60.0
    sec = seconds/ 3600.0
    return round (degree + min + sec, 5)
    
def main(image_path):
    try: ## it works on JPG(Joint photographic Experts Group)
        set = Image.open("C:\\Users\\heman\\OneDrive\\Documents\\SEM 7\\LP4\\image\\img2.jpg")
        exifdata = set._getexif()
        
        for key, value in exifdata.items():
            decode = TAGS.get(key, key)
            data = exifdata.get(key)
            resultant = f"{decode:25} : {data}"
            print(resultant)
        print("\n")
        
        for indx, tag in TAGS.items(): ## to get the GPS location of a device
            if tag== "GPSInfo":
                if indx not in exifdata:
                    raise ValueError("No EXIF gps tag found")
            
            for key, val in GPSTAGS.items():
                if key in exifdata[indx]:
                    gps_result = f"{val}: {exifdata[indx][key]}" ## printing the GPS location
                    print(gps_result)
            
            latitude=list(exifdata[indx][2])
            longitude = list(exifdata[indx][4])

            lat = convert_lat_long (latitude [0], latitude [1],latitude[2])##### for latitude
            
            long = convert_lat_long (longitude[0],longitude [1], longitude [2]) ##### for longitude print(lat long)
            
            geo= geoloaction (lat, long)
            
            print("\n")
            
            print(f"Location information: {geo}")

    except Exception as e:
        print(e)
        # sys.exit("an exception has occurred !")

def geoloaction(latitude, longitude):
    geoloacter = Nominatim(user_agent="metadata_extract")
    time.sleep(1)
    
    try:
        return geoloacter.reverse(f"{latitude}, -{longitude}").address

    except:
        return geoloaction(latitude,longitude)
    
if __name__ == '__main__':
    result = pyfiglet.figlet_format("Forensic") 
    print(result) 
    x = image()
    print(x)