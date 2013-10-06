# -*- coding: utf-8 -*-

import re;
import urllib2;
import os;
import base64;

def get_kuaichuan_url(src_url):
  kuaichuan_re='<a\sxsid=".*?"\sstyle=".*?"\sclass=".*?"\shref="(?P<url>.*?)"\stitle=".*?"\sfile_size=".*?"\starget=".*?">.*?</a>';
  req=urllib2.Request(src_url);
  req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4")
  resp=urllib2.urlopen(req).read();
  found=re.finditer(kuaichuan_re,resp,re.S);
  for url in found:
    print '快传链接';
    print url.group('url');
    print '\n';
    
def get_qq_url(src_url):
  print 'qq转真实链接:'
  url=src_url[7:len(src_url)];
  real_url=base64.decodestring(url);
  print real_url;
  
def get_thunder_url(src_url):
  print 'thunder转真实链接:'
  url=src_url[10:len(src_url)]
  tmp_url=base64.decodestring(url);
  real_url=tmp_url[2:len(tmp_url)-2];
  print real_url;
  
def get_flash_get(src_url):
  print 'flashget转真实链接:';
  url=src_url[11:len(src_url)];
  tmp_url=base64.decodestring(url);
  real_url=tmp_url[10:len(tmp_url)-10]
  #print tmp_url;
  print real_url;
  
def magnet_to_torrent(src_url):
  print '磁链转种子:';
  url=src_url[20:];
  tmp_url=url.upper();
  real_url='http://bt.box.n0808.com/'+tmp_url[0:2]+'/'+tmp_url[len(tmp_url)-2:]+'/'+tmp_url+'.torrent';
  #print url;
  print real_url;
  
#magnet:?xt=urn:btih:f8181597b51c157fb470e5ee236e364c6fbc2af2
#Thunder://QUFodHRwOi8vaW0uYmFpZHUuY29tL2luc3RhbGwvQmFpZHVIaS5leGVaWg==
#Flashget://W0ZMQVNIR0VUXWh0dHA6Ly9pbS5iYWlkdS5jb20vaW5zdGFsbC9CYWlkdUhpLmV4ZVtGTEFTSEdFVF0=&yinbing1986
#qqdl://aHR0cDovL2ltLmJhaWR1LmNvbS9pbnN0YWxsL0JhaWR1SGkuZXhl
#http://kuai.xunlei.com/d/uKx8AAJlFgBh3khS998

def choose_method(src_url):
  myurl=src_url.lower();
  thunder_re='thunder://.*?==';
  qq_re="qqdl://.*?";
  flashget_re='flashget://.*?';
  kuaichuan_re='http://kuai.xunlei.com/.*?';
  magnet_re='magnet:\?xt=urn:btih:.*?';
  if re.search(thunder_re,myurl):
    get_thunder_url(src_url);
  elif re.search(qq_re,myurl):
    get_qq_url(src_url);
  elif re.search(flashget_re,myurl):
    get_flash_get(src_url);
  elif re.search(kuaichuan_re,myurl):
    get_kuaichuan_url(src_url);
  elif re.search(magnet_re,myurl):
    magnet_to_torrent(src_url);
  else:
    print '链接不在转换范围内';
  
if __name__=='__main__':
  src_url=raw_input(u'url:');
  choose_method(src_url);
  

