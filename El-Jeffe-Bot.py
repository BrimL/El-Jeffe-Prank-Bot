import time
from slackclient import SlackClient

SLACK_TOKEN = ''
#For messing with Jeff add his name and slack profile picture URL
display_name = ''
profile_pic = ''

jeff_command = "who broke"
slack_client = SlackClient(SLACK_TOKEN)
READ_WEBSOCKET_DELAY = 1

def parse_slack_output(slack_rtm_output):
  output_list = slack_rtm_output
  if output_list and len(output_list) > 0:
    for output in output_list:
      if output and 'text' in output and jeff_command in output['text']:
        slack_client.api_call("chat.postMessage",channel=output['channel'],as_user=False, unfurl_media=True,username=display_name,icon_url=profile_pic,
          attachments = [{
            "title": 'It was me.... Jeff!',
            "image_url": 'http://dl.dropboxusercontent.com/s/mniqk7cbwgt7bdo/20170117_151614.gif?dl=0?raw=1',
            "footer": "This message approved by %s and The Mey-Meys." % display_name,
            "footer_icon": profile_pic
          }])

if __name__ == '__main__':
  if slack_client.rtm_connect():
    print("EL Jeffe has connected and is now running!")
  #RTM Connection
  if slack_client.rtm_connect():
    while True:
      parse_slack_output(slack_client.rtm_read())
      time.sleep(READ_WEBSOCKET_DELAY)
  else:
    print("RTM Connection Failure. Check Token, try again.")