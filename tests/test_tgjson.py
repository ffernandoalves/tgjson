import tgjson

import datetime
import pyrogram

class TestTgJSON:
    data = {
        'mime_type': 'video/mp4',
        'media_type': pyrogram.enums.MessageMediaType.VIDEO,
        'date': datetime.datetime(2023, 4, 28, 3, 27, 59)
    }

    dumps_out = '{"mime_type": "video/mp4", "media_type": {"pyrogram_media_type": "MessageMediaType.VIDEO", "__extended_json_type__": "MessageMediaType"}, "date": {"datetime": "2023-04-28 03:27:59", "__extended_json_type__": "datetime"}}'

    def test_dumps(self):
        assert tgjson.dumps(self.data) == self.dumps_out

    def test_loads(self):
        assert tgjson.loads(self.dumps_out) == self.data