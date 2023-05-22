import requests

api_endpoint = "https://nubela.co/proxycurl/api/linkedin/profile/resolve"
api_key = "tKsS1B1OtvqMTFymzvIFvQ"
header_dic = {"Authorization": "Bearer " + api_key}
params = {
    "company_domain": "gatesfoundation.org",
    "first_name": "Bill",
    "enrich_profile": "enrich",
    "location": "Seattle",
    "title": "Co-chair",
    "last_name": "Gates",
}
response = requests.get(api_endpoint, params=params, headers=header_dic)
