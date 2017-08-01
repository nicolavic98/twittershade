# twitter
import io
import json
import twitter


# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
#
# See https://vimeo.com/79220146 for a short video that steps you
# through this process
#
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.


CONSUMER_KEY = 'NaSlN5bA7hhc2RVChraHRJr2h'
CONSUMER_SECRET = 'SuUX64fEW0OuQpHGRjTWvadlyDTg3yXtvyxk3zsXZnpnA7vTWX'
OAUTH_TOKEN = '803517278-2JANsR8XTW6ZTgcIPwRLstgf9kRu1CVFxknPzxce'
OAUTH_TOKEN_SECRET = 'VFzfYcw0FYn9RFnG3MQomcLsES8lV3AJCJW0MEZpj7Sea'

# The keyword query

QUERY = 'lebron james'

# The file to write output as newline-delimited JSON documents
OUT_FILE = QUERY + ".json"


# Authenticate to Twitter with OAuth

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# Create a connection to the Streaming API

twitter_stream = twitter.TwitterStream(auth=auth)


print 'Filtering the public timeline for "{0}"'.format(QUERY)

# See https://dev.twitter.com/docs/streaming-apis on keyword parameters

stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document.

with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text']
