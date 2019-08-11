import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
# def Url_detail(urls):

#     for index in urls:
#         res=requests.get(index)
#         soup=BeautifulSoup(res.text,"html.parser")
#         print (soup)

# pprint(Url_detail(url_list))
url="https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")


main_data_div=soup.find("div",class_="_3RA-")
# all_pickel_data=main_data_div.findAll("div",class_="_1fje")
for index in main_data_div:
        for i in index:
                # for j in i:
                URL = i.find("a")
                pickelurl="https://paytmmall.com"+URL["href"]
                print pickelurl

                pickel_name=i.find("div",class_="_3nWP")
                print pickel_name.img["alt"]


                pickel_image_url=pickel_name.img["src"]
                print pickel_image_url

                # print j       
                print "333333333333333333333333333333333333333333333"
                print "================================================="
        print "------------------------------------"

        # all_pickel=index.find("div",class_="_2i1r")
        # # for i in all_pickel:
        # URL = all_pickel.a["href"]
        # pickelurl="https://paytmmall.com"+URL
            print pickelurl

        # pickel_name=all_pickel.find("div",class_="_3nWP")
        # print pickel_name.img["alt"]


        # pickel_image_url=pickel_name.img["src"]
        # print pickel_image_url










#     pickel=all_pickel_data.find("div",class_="_3WhJ").a.get_text()
#     print pickel
#     print all_pickel_data
# particular_pickel=all_pickel_data.find("div",class_="_2i1r").get_text()
# print particular_pickel


# for one_pickel in main_data_div:
#     pickel_group=one_pickel.find("div",class_="_1fje").get_text()
#     print pickel_group
    # for one_pickel in pickel_group:
    #     particular_pickel=one_pickel.find("div",class_="_2i1r").get_text()
    #     print particular_pickel
    # for pickel in particular_pickel:
        # j=pickel.find("div",class_=)
