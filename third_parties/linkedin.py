import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    api_key = os.environ.get("PROXYCURL_API_KEY")

    header_dic = {"Authorization": f"Bearer {api_key}"}

    params = {
        "url": linkedin_profile_url,
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic)

    data = response.json()

    data = {
        k: v for k, v in data.items() if v not in [[], "", None] and k not in  ["people_also_viewed", "certifications", "similarly_named_profiles"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
