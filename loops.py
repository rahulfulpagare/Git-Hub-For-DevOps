list_of_cloud = ["aws","azure","gcp","digital ocean","utho","alibaba","oracle"]
cloud = "gcp" #variable

print(list_of_cloud)
#add a new cloud salesforce
list_of_cloud.append("salesforce")

print(list_of_cloud)
#add a new cloud IBM
list_of_cloud.append("IBM")

print(list_of_cloud)
#add a new cloud eNlight
list_of_cloud.append("eNlight")

print(list_of_cloud)
list_of_cloud.insert(7,"Heroku")

print(list_of_cloud)
print(len(list_of_cloud))

list_of_cloud.insert(0,"hello cloud")

print(list_of_cloud)

for cloud in list_of_cloud:
    print(6)
    print(cloud)

for i in range (1,11):
     print(ram)