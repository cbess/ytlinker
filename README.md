YouTube Linker
==============

Provides full title text for YouTube videos.


Requirements
------------

 * Flask 0.7.x
 * AppSpot environment


Back story and purpose
----------------------

Problem: The YouTube app does not display the entire video title in the playlist.

    *YouTube video title:
        This is a long title that is common for me part 1 of 7
        This is a long title that is common for me part 2 of 7
        
    *Displays as:
        This is a long title...
        This is a long title...

The final output does not help me find the next video. 
Even worst, YouTube does not always place the videos in order.

Background:
I made this for two reasons:
    1. I became frustrated with the truncated links on the iPad YouTube app
    2. I was about to each in an hour and wanted to watch videos while I prepared my food.
    
This is my first time using App Spot (I finally used my account) and my first Flask app deployed (I usually work with Django).
This only took me ~45 mins to commit and deploy (from thought to appspot). I plan on working on it upon request or when I need an update.

This works best for folks who use a mobile device watch videos within playlists on YouTube.

What I learned:
    * Google AppSpot is crazy awesome for quick apps.
    * Flask is banging.
    * AppSpot + Flask == All the speed of PHP deployments with none of the disadvantages (to many to name).
 

Author and license
------------------

[yt-linker](https://github.com/cbess/ytlinker),
Copyright 2011, [C. Bess](http://cbess.blogspot.com)

Licensed under the MIT