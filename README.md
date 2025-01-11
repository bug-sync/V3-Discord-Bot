# V3-Discord-Bot
A simple bot I made for me and friends. Currently only has AI chat support (thank you Xtr4F for pycharacterai!!), but I do plan on adding more soon!

## Setup
Make sure you have Python installed + added to path, then run the following commands in cmd...

`pip install discord`

`pip install git+https://github.com/Xtr4F/PyCharacterAI`

Now, open V3.py. Near the top you should see `dctoken` and `caitoken`. Replace these with your tokens-- Discord can be found in the bot dev portal. For Character.AI you'll need to open your browser's developer tools (`F12`, `Ctrl+Shift+I`, or `Cmd+J`), go to the `Network` tab, look for `Authorization` in the request header (you may have to interact with the site..), and copy the value after `Token`.
## How To Use
Your server will need a channel with the name `chat` (for communicating with the AI) and a channel called `character-id-submissions` (to change the character). Type anything in the `chat` channel (with the program running ofc), and you should get a response! 

To change the bot, go to `character-id-submissions` and paste the ID. The ID is the end part of the Character.AI URL, as seen highlighted in the image.

![image](https://github.com/user-attachments/assets/3189685e-f61b-48f7-b006-9ebfb7ca8a61)

If you'd like to say something WITHOUT a response (and refuse to leave the channel, you lazy bum..) you can simply append ((OOC)) to the beginning of your message.

You can also change the default character, chat channel, OOC/no response keyword, ID change channel, etc by editing their respective values in the code..!
