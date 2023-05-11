# tgjson



## Install

cloning the repository:
```
git clone github.com/ffernandoalves/tgjson.git
cd tgjson
python3.11 -m venv env
env/bin/activate
python setup.py install
```


## To Use

```python
import tgjson
import datetime
import pyrogram

data = {
        'mime_type': 'video/mp4',
        'media_type': pyrogram.enums.MessageMediaType.VIDEO,
        'date': datetime.datetime(2023, 4, 28, 3, 27, 59)
    }
dumps_out = tgjson.dumps(data)
load_out = tgjson.loads(dumps_out)
```