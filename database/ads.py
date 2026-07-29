ADS = [
    {
        "id": 1,
        "title": "BRH Sponsor",
        "type": "video",
        "url": "",
        "duration": 15,
        "active": True,
    }
]


def get_ads():
    return [ad for ad in ADS if ad["active"]]


def get_ad(ad_id):
    for ad in ADS:
        if ad["id"] == ad_id:
            return ad

    return None


def add_ad(ad):
    ADS.append(ad)


def disable_ad(ad_id):
    ad = get_ad(ad_id)

    if ad:
        ad["active"] = False
