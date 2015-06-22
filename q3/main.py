__author__ = 'bj'

"""Test a SOAP call function by comparing the response to a string.

There are two main functions: The SOAP call: get_uk_location_by_postcode() and the test framework: test_soap_call

Actual XML Element Tree comparison is difficult, so I have presented three different approaches:
    Serialisation using a common parser - serialise_and_compare()
    Compare all nodes regardless of order - compare_xpaths()
    Show what is actually different using two tree analysis algorithms - xmldiff_compare()
Which to use will depend on the context.
"""

import xml.etree.ElementTree as ET
from pysimplesoap.client import SoapClient
from pyxmldiff.xmldiff import xmlDiff


def get_uk_location_by_postcode(county):
    client = SoapClient(wsdl="http://www.webservicex.net/uklocation.asmx?WSDL", trace=False)

    try:
        results = client.GetUKLocationByCounty(county)
    except:
        # save sent and received messages for debugging:
        open("request.xml", "w").write(str(client.xml_request))
        open("response.xml", "w").write(str(client.xml_response))
        raise

    return results['GetUKLocationByCountyResult']


def get_file_as_string(filename):
    str_data = ""
    with open(filename, 'r') as f:
        for x in f.readlines():
            str_data += x
    return str_data


def serialise_and_compare(a, b):
    return a.tostring() == b.tostring()


def xmldiff_compare(a, b):
    results = xmlDiff(a, b)
    if results:
        print(results)
        return False
    return True


def compare_xpaths(a, b):
    return sorted(list_of_xpaths(a)) == sorted(list_of_xpaths(b))


def list_of_xpaths(root):
    result = ['/' + root.tag + '/' + (root.text or '').strip()]
    for child in root.getchildren():
        for xpath in list_of_xpaths(child):
            result.append('/' + root.tag + xpath)
    return result


def test_soap_call(soap_call, expected_response, *args):
    """Test a SOAP call function by comparing the response to a string.
    Actual XML Element Tree comparison is difficult, so I have presented three different approaches:
        Serialisation using a common parser - serialise_and_compare
        Compare all nodes regardless of order - compare_xpaths
        XMLDiff - to show what is actually different using two tree analysis algorithms
    Which to use will depend on the context.
    :param soap_call type:function
    :param expected_response type:str
    :param args type:[str]
    """
    expected_et = ET.fromstring(expected_response)
    actual_et = ET.fromstring(soap_call(*args))
    if xmldiff_compare(expected_et, actual_et):
        print("Given string forms a matching XML element tree. PASS")
    else:
        print("Given string does not form a matching XML element tree! FAIL")


if __name__ == '__main__':
    test_data = get_file_as_string('./tests/cumbria_response.xml')
    test_soap_call(get_uk_location_by_postcode, test_data, 'Cumbria')
