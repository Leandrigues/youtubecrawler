from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req 

viewFirst = []
likes = []
dislikes = []
playlistUrls = [] # Insert the ID of the playlist (for example:
# the ID of https://www.youtube.com/watch?v=Qyclqo_AV2M&list=PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc is PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc)
for url in (playlistUrls):
    urlPlaylist = "https://m.youtube.com/playlist?list="+url
    client = req(urlPlaylist)
    pageHtml = client.read()
    client.close()
    pageSoup = soup(pageHtml, "html.parser")
    paragraph = pageSoup.findAll("a", href=True)
    playlists = []
    watchList = []
    videosUrl = pageSoup.find_all('a', {'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '})

    for link in (videosUrl):
        watchList.append(link['href'])
        name = link.text.strip()
        # print(name) # Uncomment to print the name of the videos
        
    for link in watchList:
        urlWatch = "https://m.youtube.com/"+link
        newClient = req(urlWatch)
        newPageHtml = newClient.read()
        newClient.close()
        newPageSoup = soup(newPageHtml, "html.parser")
        likeList = newPageSoup.findAll('button', { "class" : "yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip"})
        dislikeList = newPageSoup.findAll('button', {"class":"yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip"})
        # LIKES AND DISLIKES 
        for like in (likeList):
            # print(like. text, end=",") # Uncomment to print likes. Insert "end=','" to separate in columns into a .csv
            likes.append(like.text)
        for dislike in (dislikeList):
            # print(dislike.text) # Uncomment to print dislikes 
            dislikes.append(dislike.text)

        # VIEWS
        views = newPageSoup.findAll('div')
        viewsList = []
        for item in (views):
            item = item.text.split()
            for i in range(len(item)):
                if item[i] == ' ' or item[i] == '' or item[i] == '\n':
                    item.pop([i])
            if 'views' in item and item[-2][0] in ['0','1','2','3','4','5','6','7','8','9']:
                viewsList.append(item[-2])
                break
        if viewsList != []:
            viewFirst.append(viewsList[0])
        # print(viewFirst) # Uncomment to print the views of the videos



