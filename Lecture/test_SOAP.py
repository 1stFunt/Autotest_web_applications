from zeep import Client
wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = "здесь должна быть подпись для корректной работы теста"

client = Client(wsdl=wsdl)


def test_step1():
    assert client.service.VerifySignature('CMS', sign)['Result']
