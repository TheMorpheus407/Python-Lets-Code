from torpy import TorClient
from torpy.utils import recv_all
from torpy.http import requests
from torpy.http.adapter import TorHttpAdapter

host = "ifconfig.me"
with TorClient() as tor:
    with tor.create_circuit(3) as circ:
        with circ.create_stream((host, 80)) as stream:
            stream.send(b'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host.encode())
            ret = recv_all(stream).decode()
            print(ret)

host2 = 'https://www.facebookcorewwwi.onion/'
with TorClient() as tor:
    with tor.get_guard() as guard:
        adapter = TorHttpAdapter(guard, 3)
        with requests.Session() as sess:
            sess.headers.update({'User-Agent': 'Mozilla/5.0'})
            sess.mount('http://', adapter)
            sess.mount('https://', adapter)

            resp = sess.get("http://" + host, timeout=15)
            print(resp.text)

            resp = sess.get(host2)
            print(resp.text)