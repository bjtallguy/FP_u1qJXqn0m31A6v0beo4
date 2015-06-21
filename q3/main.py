__author__ = 'bj'

import xml.etree.ElementTree as ET
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

    return results['GetUKLocationByCountyResult']


def get_file_as_string(filename):
    str_data = ""
    with open(filename, 'r') as f:
        for x in f.readlines():
            str_data += x
    return str_data


def test_soap_call(soap_call, expected_response, *args):
    """Test a SOAP call function by comparing the response to a string.
    Actual XML Element Tree comparison is difficult, so I have parsed both the fresh response and recorded response
    using an XML parser known to maintain order (Python's XParse); then compared the serialised output of each.
    :param soap_call type:function
    :param expected_response type:str
    :param args type:[str]
    """
    expected_et = ET.fromstring(expected_response)
    response_et = ET.fromstring(soap_call(*args))
    try:
        assert ET.dump(response_et) == ET.dump(expected_et)
    except AssertionError:
        print("Given string does not form a matching XML element tree! FAIL")
    else:
        print("Given string forms a matching XML element tree. PASS")


if __name__ == '__main__':
    test_data = get_file_as_string('./tests/cumbria_response.xml')
    test_soap_call(get_uk_location_by_postcode, test_data, 'Cumbria')
