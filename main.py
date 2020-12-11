from twisted.internet import protocol, reactor, endpoints
import pyfiglet

def can_utf8_decode(data):
    try:
        data.decode("utf-8")
        return True
    except:
        return False

def findClientFont(clients, client):
    for i in clients:
        if(i["client"] == client):
            return i["font"]

class Figlet(protocol.Protocol):
    def __init__(self):
        self.font = "standard"
    
    def dataReceived(self, data):
        if(not data or not can_utf8_decode(data)):
            return
        data = data.decode()
        if(data.startswith("/font ")):
            try:
                font = data.split("/font")[1].replace(" ", "").replace("\r", "").replace("\n", "")
                # Test if the font is valid
                pyfiglet.figlet_format("test", font=font)
                self.font = font
                self.transport.write(b"OK")
            except:
                self.transport.write(b"ERROR")
            finally:
                self.transport.write(b"\n")
                return
        if(data.startswith("/fonts")):
            self.transport.write("\n".join(pyfiglet.Figlet().getFonts()).encode())
            self.transport.write(b"\n")
            return
        if(data.startswith("/help")):
            self.transport.write(pyfiglet.figlet_format("Figlet-Telnet").encode())
            self.transport.write(b"Simply type the message to convert it to ASCII art.\nTo change the font, type: /font [name]\nIf you want to see a list of all available fonts, type: /fonts\nTo exit, type: /exit")
            self.transport.write(b"\n")
            return
        if(data.startswith("/ping")):
            self.transport.write(b"PONG")
            self.transport.write(b"\n")
            return
        if(data.startswith("/exit")):
            self.transport.write(b"BYE")
            self.transport.write(b"\n")
            self.transport.loseConnection()
            return
        result = pyfiglet.figlet_format(data, font=self.font)
        self.transport.write(result.encode())


class FigletFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Figlet()

endpoints.serverFromString(reactor, "tcp:23").listen(FigletFactory())
print("Ready")
reactor.run()
