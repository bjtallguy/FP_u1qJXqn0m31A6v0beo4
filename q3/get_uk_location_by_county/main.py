__author__ = 'bj'

from pysimplesoap.client import SoapClient


def get_uk_location_by_postcode(county):
    client = SoapClient(wsdl="http://www.webservicex.net/uklocation.asmx?WSDL", trace=False)

    try:
        results = client.GetUKLocationByCounty(county)
    except:
        # save sent and received messages for debugging:
        open("request.xml", "w").write(client.xml_request)
        open("response.xml", "w").write(client.xml_response)
        raise

    # extract the result:
    ta = results['GetUKLocationByCountyResult']  # .encode("utf-8")
    return ta


def test_soap_call(soap_call, expected_response, params=None):
    assert soap_call(params) == expected_response


if __name__ == '__main__':
    import xml.etree.ElementTree as ET


    tree = ET.parse('country_data.xml')
    root = tree.getroot()
    print(get_uk_location_by_postcode("cumbria"))
