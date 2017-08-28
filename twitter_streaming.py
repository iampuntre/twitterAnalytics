#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "77986695-MYT3r7DeYhPMuqz1Awb67uPYmsNYrzjNCi4J1q5pG"
access_token_secret = "og5k6xWNZKB1hadzoAWKMTxoc2THvWoXhit2DknBjlWR1"
consumer_key = "WOn9ZXqqXhIUIiRjKfLuv5Wws"
consumer_secret = "MED8GUsKsTejzYaMAiS32RnxsBtiVZIkNQOi9RPBAiRXe3MQrN"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
