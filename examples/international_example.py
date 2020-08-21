import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.international_street import Lookup as InternationalLookup


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)
    client = ClientBuilder(credentials).with_licenses(['international-fake'])\
        .build_international_street_api_client()

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/cloud/international-street-api#http-input-fields

    lookup = InternationalLookup()
    lookup.input_id = "ID-8675309"
    lookup.geocode = True  # Must be expressly set to get latitude and longitude.
    lookup.organization = "John Doe"
    lookup.address1 = "Rua Padre Antonio D'Angelo 121"
    lookup.address2 = "Casa Verde"
    lookup.locality = "Sao Paulo"
    lookup.administrative_area = "SP"
    lookup.country = "Brazil"
    lookup.postal_code = "02516-050"

    candidates = client.send(lookup)  # The candidates are also stored in the lookup's 'result' field.

    first_candidate = candidates[0]
    print("Address is {}".format(first_candidate.analysis.verification_status))
    print("Address precision: {}\n".format(first_candidate.analysis.address_precision))

    print(u"First Line: {}".format(first_candidate.address1))
    print(u"Second Line: {}".format(first_candidate.address2))
    print(u"Third Line: {}".format(first_candidate.address3))
    print(u"Fourth Line: {}".format(first_candidate.address4))
    print("Latitude: {}".format(first_candidate.metadata.latitude))
    print("Longitude: {}".format(first_candidate.metadata.longitude))


if __name__ == "__main__":
    run()
