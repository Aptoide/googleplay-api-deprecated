from gpapi.googleplay import GooglePlayAPI, RequestError
import json

server = GooglePlayAPI(debug=True, locale='id-ID')
server.login(
    None, None,
    int('3d9dadcd34b1d5bf', 16),
    'vAVzTIwkcGaYMqtXiOLtk-ty7Jwj5IltXs4o23oPDO3g5GPidel9ktzaVwPnZnQVX-n3eA.'
)

details = server.details('com.snapchat.android')
print(json.dumps(details, sort_keys=True, indent=4))
