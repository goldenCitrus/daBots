"""Holds the information object"""
class Information:
    """holds message,client and bodid info"""
    def __init__(self, message, client=None, botid=None):
        self.message = message
        self.client = client
        self.botid = botid

        self.return_message = ''
        self.chandler = False
        self.last_ihkh = -1
