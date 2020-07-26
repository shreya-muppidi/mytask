import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect
parser=argparse.ArgumentParser()
parser.add_argument('--page_num_max', help='enter the number of paages to parse', type=int) 
parser.add_argument('--dbname', help='enter the name of the database', type=str) 
args=parser.parse_args()
scraped_list=[]
oyo_url='http://www.oyorooms.com/hotels-in-bangalore/?page=' 
page_num_max=args.page_num_max
connect.connect(args.dbname)
for page_num in range(1,page_num_max):
    req=requests.get(oyo_url,str(page_num)) 
    content=req.content 
    soup=BeautifulSoup(content,'html.parser')
    all_hotels=soup.find_all('div',{'class':'hotelCardListing'}) 
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict['name']= hotel_name=hotel.find('h3',{'class':'listingHotelDescription__HotelName'}).text
        hotel_dict['address']=hotel_address=hotel.find('span',{'itemprop':'streetAddress'}).text 
        try:
            hotel_dict['rating']=hotel_rating=hotel.find('span',{'class':'listingPrice__ratingSummary'}).text 
        except AttributeError:
            pass

        amenities_list=[]
        parent_amenities=hotel.find('div',{'class':'amenityWrapper'})
        for amenity in parent_amenities.find_all('div',{'class':'amenityWrapper__amenity'}):
            amenities_list.append(amenity.find('span',{'class':'d-body-sm'}).text.strip()) 
        #print(hotel_name,hotel_address,hotel_rating,amenities_list) 
        hotel_dict['amenities']=', 'join(amenities_list[:-1])
        scraped_list.append(hotel_dict) 
        connect.insert_into_table(args.dbname,tuple(hotel_dict.values()))
dataFrame=pandas.DataFrame(scraped_list) 
dataFrame.to_csv('oyo.csv') 
connect.get_hotel_info(args.dbname)
