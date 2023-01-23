from pushbullet import Pushbullet

API_KEY = "o.FzG5R98RtBZNtdbuv7956RgDupSZW5K8"
file = "resolutions.txt"


with open (file,mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note('Please remember',text)