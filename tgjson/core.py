import json
import datetime
import pyrogram

__all__ = ["TgJSON"]

class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)
        
class TgJSON:
    """
    use
    >>> data = {
    ...     'mime_type': 'video/mp4',
    ...     'media_type': pyrogram.enums.MessageMediaType.VIDEO,
    ...     'date': datetime.datetime(2023, 4, 28, 3, 27, 59)}
    >>> encode = json.dumps(data, cls=TgJSON.Encoder)
    >>> decode = json.loads(encode, cls=TgJSON.Decoder)
    """

    _datetime = "datetime"
    _media_type = "pyrogram_media_type"

    class Encoder(ExtendedEncoder):
        def encode_datetime(self, _datetime):
            return {TgJSON._datetime: str(_datetime)}
        
        def encode_MessageMediaType(self, media):
            return {TgJSON._media_type: str(media)}
        
    class Decoder(ExtendedDecoder):
        def decode_datetime(self, _datetime):
            return datetime.datetime.fromisoformat(_datetime[TgJSON._datetime])
        
        def decode_MessageMediaType(self, _media_type):
            return getattr(pyrogram.enums.MessageMediaType, _media_type[TgJSON._media_type].split('.')[-1])
    
