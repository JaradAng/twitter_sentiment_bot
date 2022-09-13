import tweepy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']