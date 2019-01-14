"""Restaurant rating lister."""


# put your code here
def rest_ranking(textfile):
    rankings_dict = {}
    file_content = open(textfile)
    for line in file_content:
        line = line.rstrip()
        restname = line.split(":")[0]
        ranking = line.split(":")[1]
        rankings_dict[restname] = ranking

    file_content.close()
    for restaurant in sorted(rankings_dict.items()):
        print("{} is rated at {}".format(restaurant[0],restaurant[1]))