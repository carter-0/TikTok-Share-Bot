import random
import requests
import threading
from time import time, sleep

def main(amount, video_id):
  action_time = round(time())
  device_id = ''.join(random.choice('0123456789') for _ in range(19))

  data = (
            f'action_time={action_time}&item_id={video_id}&item_type=1&share_delta=1&stats_cha'
            'nnel=embed'
        )
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'x-common-params-v2': 'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&devi'
                            f'ce_id={device_id}&aid=1233&os_version=13.5.1&device_platform=ip'
                            'hone&device_type=iPhone10,5'
  }

  try:
      response = requests.post(
                'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region='
                'SE&app_skin=white&', data=data, headers=headers
      )
  except Exception as e:
      print(f'Error: {e}')
  
if __name__ == '__main__':
  start_time = time()
  amount = int(input("How many times should it be shared? >>> "))
  video_id = input('TikTok Video URL to be Shared >>> ').split('/')[5]

  for i in range(amount):
      while True:
          if threading.active_count() <= 300:
              threading.Thread(target=main, args=(amount, video_id)).start()
              break
  sleep(3)
