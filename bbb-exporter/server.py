import logging
from time import sleep

from prometheus_client import start_http_server, REGISTRY

import settings
from collector import BigBlueButtonCollector

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s")


if __name__ == '__main__':
    if settings.DEBUG:
        logging.getLogger().setLevel(logging.DEBUG)

    start_http_server(settings.PORT, addr=settings.BIND_IP)
    logging.info("HTTP server started on port: {}".format(settings.PORT))

    collector = BigBlueButtonCollector()

    if len(settings.ROOM_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_participants_buckets(settings.ROOM_PARTICIPANTS_CUSTOM_BUCKETS)

    if len(settings.ROOM_LISTENERS_CUSTOM_BUCKETS) > 0:
        collector.set_room_listeners_buckets(settings.ROOM_LISTENERS_CUSTOM_BUCKETS)

    if len(settings.ROOM_VOICE_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_voice_participants_buckets(settings.ROOM_VOICE_PARTICIPANTS_CUSTOM_BUCKETS)

    if len(settings.ROOM_VIDEO_PARTICIPANTS_CUSTOM_BUCKETS) > 0:
        collector.set_room_video_participants_buckets(settings.ROOM_VIDEO_PARTICIPANTS_CUSTOM_BUCKETS)

    REGISTRY.register(collector)
    while True:
        sleep(1)
