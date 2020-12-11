# telnet-figlet
Figlet in Telnet!<br>
To run it, install Python (3.9 is recommended) and Telnet and install the requirements with pip(<code>pip install -r requirements.txt</code>).<br>
And then type:<br>
<code>python main.py # or python3 main.py</code>
<br>
Now, you can do <code>telnet localhost</code> to connect to your server. Type /help for a list of commands you can run.
<br>
You can also run it with Docker:<br>
<code>docker build -t telnet-figlet . # to build the image</code>
<br>
<code>docker run -p 23:23 --rm telnet-figlet # to run the image. You can also add -d to run it in the background(it is recommended to remove --rm after that).</code>
