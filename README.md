# lyric-analysis

This program is used to determine the uniqueness of lyrics in music. If there is a lot of repetition of a word, then the percentage of unique lyrics will be lower, and if there is less repetition it will be higher.

![screenshot](https://i.imgur.com/cemxEm3.png)

In order to run this program, the `requests`, `beautifulsoup4`, and `lyricsgenius` libraries have to be installed. You can do this with PIP. 

After this, you can `git clone` this repository.

Then, generate a token to use the Genius lyrics API [here](https://genius.com/api-clients/new). If you don't have an account already, it will ask you to make one. For the app website URL and redirect URI, you can link to a random website, if you don't have something specific you want to put instead. Click save, then generate access token. Copy and paste this token into the `TOKEN` variable in main.py, in quotes.

Now, you can run the program by running main.py. Follow the prompts, and see the uniqueness in the lyrics of your favorite music!
