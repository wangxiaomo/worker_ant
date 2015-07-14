# coding: utf8

import requests
import lxml.html


def strip(s):
    return s.strip() if s else ''

def save_ip_list(ips):
    with open("ip.txt", "a") as f:
        f.writelines(("%s\n" % i for i in ips if i))

def get_cn_proxy_list():
    r = requests.get("http://cn-proxy.com/")
    doc = lxml.html.fromstring(r.text)
    trs = doc.xpath("//table/tbody/tr")
    ips = []
    for tr in trs:
        items = tr.xpath("./td/text()")
        ip = "http:%s:%s" % (strip(items[0]), strip(items[1]))
        ips.append(ip)
    return ips

def get_kuaidaili_list():
    # 取前10页
    ips = []
    for i in range(1, 11):
        url = "http://www.kuaidaili.com/proxylist/%s/" % i
        r = requests.get(url)
        doc = lxml.html.fromstring(r.text)
        trs = doc.xpath("//table/tbody/tr")
        for tr in trs:
            items = tr.xpath("./td/text()")
            ip = "http:%s:%s" % (strip(items[0]), strip(items[1]))
            ips.append(ip)
    return ips

def get_haodaili_guonei_list():
    ips = []
    for i in range(1, 101):
        url = "http://www.haodailiip.com/guonei/%s" % i
        r = requests.get(url)
        doc = lxml.html.fromstring(r.text)
        trs = doc.xpath("//table[@class='proxy_table']/tr")
        for tr in trs[1:]:
            items = tr.xpath("./td/text()")
            ip = "http:%s:%s" % (strip(items[0]), strip(items[1]))
            ips.append(ip)
    return ips

def get_haodaili_guowai_list():
    ips = []
    for i in range(1, 101):
        url = "http://www.haodailiip.com/guoji/%s" % i
        r = requests.get(url)
        doc = lxml.html.fromstring(r.text)
        trs = doc.xpath("//table[@class='proxy_table']/tr")
        for tr in trs[1:]:
            items = tr.xpath("./td/text()")
            ip = "http:%s:%s" % (strip(items[0]), strip(items[1]))
            ips.append(ip)
    return ips

save_ip_list(get_cn_proxy_list())
save_ip_list(get_kuaidaili_list())
save_ip_list(get_haodaili_guonei_list())
save_ip_list(get_haodaili_guowai_list())
