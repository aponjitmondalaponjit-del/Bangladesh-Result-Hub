ADS = [
    {
        "id": 1,
        "title": "BRH Premium",
        "type": "image",
        "file": "premium.jpg",
        "url": "https://t.me/YourChannel",
        "duration": 10,
        "active": True,
    },
    {
        "id": 2,
        "title": "Your Product",
        "type": "video",
        "file": "product.mp4",
        "url": "https://example.com",
        "duration": 10,
        "active": False,
    },
]


def get_ads():
    return ADS


def get_active_ads():
    return [ad for ad in ADS if ad["active"]]
