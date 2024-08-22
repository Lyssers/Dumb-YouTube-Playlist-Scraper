# Dumb YouTube Playlist Scraper

This is a very dumb basic selenium links scraper that works with YT.

Before running it read below:

## How to use:

1. Install Firefox (or change script to use a different browser)
2. Install Python
3. Install GeckoDriver
4. Install Selenium (with pip install selenium)
5. Sign in to YouTube on Firefox. Make sure you accept all cookies/stay signed in (relaunch browser and access website to verify).
6. Navigate to your Firefox profile directory (e.g. on Windows: `C:\Users\<Username>\AppData\Roaming\Mozilla\Firefox\Profiles\` where <username> is your username.)
7. Find the profile that ends in `.default`
8. Replace profile in script on line 8 with your profile.
9. In Firefox, get the URL of your playlist (e.g. Favourites playlist) and replace it at line 11
10. Depending on the amount of videos you have, you may want to increase the amount of scrolls. Since the playlist page doesn't load all at once, you have to manually scroll to the bottom. To avoid reliance on the ever changing codebase of YT and not involve weird Javascript stuff, this just scrolls however much you tell it. There's no harm in too many scrolls apart from wasted time. In my case roughly 22 scrolls was good for 2k videos.
11. Replace "links.txt" with filename where to store the links.
12. Run the script! You should see your browser pop up and you'll see it scroll down every 5s. If your page loads slower, increase the time.sleep value on line 21.
13. All the links will be in the file only once the script has finished.

Now you can do with that what you wish. E.g. you can download all the videos by running something like `cat links.txt | grep 'watch' | awk '!a[$0]++' | awk -F '&' '{print $1}' > links_angel.txt` on Linux which will deduplicate and extract only watch links from the list. Then use yt-dlp with the a switch, i.e. yt-dlp -a links_angel.txt to download it.






