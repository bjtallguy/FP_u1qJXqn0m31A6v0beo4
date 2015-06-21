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


def compare_element_trees(a, b):
    """
    Walk the entire XML element tree, in alphabetical order to elements, tags, text and tails, comparing every node.
    :param a: ElementTree
    :param b: ElementTree
    :return: bool
    """

    if a.tag != b.tag:
        return False

    if (a.text and b.text) and (a.text != b.text):
            return False
    elif b.text:
        return False

    if (a.tail and b.tail) and (a.tail != b.tail):
            return False
    elif b.tail:
        return False

    # Attributes are retirieved as a list of (name, value) pairs.
    if sorted(a.items()) != sorted(b.items()):
        return False


def xml_compare(x1, x2, reporter=None):
    if x1.tag != x2.tag:
        if reporter:
            reporter('Tags do not match: %s and %s' % (x1.tag, x2.tag))
        return False
    for name, value in x1.attrib.items():
        if x2.attrib.get(name) != value:
            if reporter:
                reporter('Attributes do not match: %s=%r, %s=%r'
                         % (name, value, name, x2.attrib.get(name)))
            return False
    for name in x2.attrib.keys():
        if name not in x1.attrib:
            if reporter:
                reporter('x2 has an attribute x1 is missing: %s'
                         % name)
            return False
    if not text_compare(x1.text, x2.text):
        if reporter:
            reporter('text: %r != %r' % (x1.text, x2.text))
        return False
    if not text_compare(x1.tail, x2.tail):
        if reporter:
            reporter('tail: %r != %r' % (x1.tail, x2.tail))
        return False

    cl1 = x1.getchildren()
    cl2 = x2.getchildren()

    if len(cl1) != len(cl2):
        if reporter:
            reporter('children length differs, %i != %i'
                     % (len(cl1), len(cl2)))
        return False

    i = 0
    for c1, c2 in zip(cl1, cl2):
        i += 1
        if not xml_compare(c1, c2, reporter=reporter):
            if reporter:
                reporter('children %i do not match: %s'
                         % (i, c1.tag))
            return False

    return True


def text_compare(t1, t2):
    if not t1 and not t2:
        return True
    if t1 == '*' or t2 == '*':
        return True
    return (t1 or '').strip() == (t2 or '').strip()


def test_soap_call(soap_call, expected_response, *args):
    """Test a SOAP call function by comparing the response to a string.
    Actual XML Element Tree comparison is difficult, so I have parsed both the fresh response and recorded response
    using an XML parser known to maintain order (Python's XParse); then compared the serialised output of each.
    :param soap_call type:function
    :param expected_response type:str
    :param args type:[str]
    """
    expected_et = ET.fromstring(expected_response)
    actual_et = ET.fromstring(soap_call(*args))
    if xml_compare(expected_et, actual_et, reporter=print):
        print("Given string forms a matching XML element tree. PASS")
    else:
        print("Given string does not form a matching XML element tree! FAIL")
        print(ET.tostring(actual_et), "\n", ET.tostring(expected_et))


if __name__ == '__main__':
    test_data = get_file_as_string('./tests/cumbria_response.xml')
    test_soap_call(get_uk_location_by_postcode, test_data, 'Cumbria')
