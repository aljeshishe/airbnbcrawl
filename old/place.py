import json
from datetime import datetime
from pathlib import Path

import click
import requests
import email

from parser import parse


results_path = Path('../results')
results_path.mkdir(parents=True, exist_ok=True)



@click.command()
@click.argument('id')
def _parse_place(id: str):
    items = parse_place(id=id)
    short_lines = [f'{item["calendarDate"]}: {item["localPriceFormatted"]} bookable:{item["bookable"]}' for item in items]
    short_content = '\n'.join(short_lines)
    print(short_content)
    (results_path / f'{id}_short.txt').write_text(short_content)
    return items


def parse_place(id: str):
#     headers = '''Host: www.airbnb.ru
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
# Accept: */*
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Referer: https://www.airbnb.ru/rooms/22943460?source_impression_id=p3_1603907925_qKOIEXsL7ZmZgxJ2&guests=1&adults=1
# Content-Type: application/json
# X-Airbnb-GraphQL-Platform: web
# X-Airbnb-API-Key: d306zoyjsyarp7ifhu67rjxn52tv0t20
# X-CSRF-Token: V4$.airbnb.ru$vNJwZHT6B5E$9-b0Gf0vD0ZX7uxtO3OqSIgt72xiPGdr4AOVYw93ceY=
# X-CSRF-Without-Token: 1
# X-Airbnb-GraphQL-Platform-Client: minimalist-niobe
# Connection: keep-alive
# Cookie: bev=1601283992_NjhkZjdjZWE1ZmI2; cdn_exp_f699727e78669251b=control; tzo=180; frmfctr=wide; OptanonConsent=landingPath=https%3A%2F%2Fwww.airbnb.ru%2Frooms%2F45087683%3Fsource_impression_id%3Dp3_1600693700_YdyIut7wxZFNuvRd%26guests%3D4%26adults%3D4%26check_in%3D2020-10-02%26check_out%3D2020-10-10&datestamp=Mon+Sep+28+2020+12%3A06%3A42+GMT%2B0300+(Moscow+Standard+Time)&version=4.6.0&groups=0_179751%3A1%2C1%3A1%2C2%3A1%2C0_183217%3A1%2C3%3A1%2C0_183345%3A1%2C0_183219%3A1%2C4%3A1%2C0_183240%3A1%2C0_179739%3A1%2C0_179743%3A1%2C0_185813%3A1%2C0_183096%3A1%2C0_179755%3A1%2C0_183215%3A1%2C0_185808%3A1%2C0_179747%3A1%2C0_179740%3A1%2C0_179744%3A1%2C0_185810%3A1%2C0_185814%3A1%2C0_183097%3A1%2C0_179756%3A1%2C0_183216%3A1%2C0_183344%3A1%2C0_185809%3A1%2C0_179748%3A1%2C0_179752%3A1%2C0_183241%3A1%2C0_179741%3A1%2C0_183098%3A1%2C0_179745%3A1%2C0_183346%3A1%2C0_185811%3A1%2C0_179737%3A1%2C0_185815%3A1%2C0_179757%3A1%2C0_179749%3A1%2C0_179753%3A1%2C0_185831%3A1%2C0_183099%3A1%2C0_179738%3A1%2C0_179742%3A1%2C0_183095%3A1%2C0_185816%3A1%2C0_183243%3A1%2C0_179754%3A1%2C0_183214%3A1%2C0_179750%3A1; cfrmfctr=DESKTOP; cbkp=4; OptanonAlertBoxClosed=2020-09-28T09:06:42.978Z; _airbed_session_id=b693486d7af95a36b7b909e1849bbf17; cdn_exp_e437bcda7f41486a6=extend_one_three_five_days; cdn_exp_14332663b5ca816ee=control; cdn_exp_b1b38777d5c7a308a=runtime_initializers; cdn_exp_b76569944fd3a6caf=extend_one_three_seven_days; sdid=; _user_attributes=%7B%22curr%22%3A%22RUB%22%2C%22guest_exchange%22%3A76.75032%2C%22device_profiling_session_id%22%3A%221602659137--04f5ace973032ed897a9569f%22%2C%22giftcard_profiling_session_id%22%3A%221603905918-7725978-0589a206b3abb80aaf076cb5%22%2C%22reservation_profiling_session_id%22%3A%221603905918-7725978-ddbef550dc21e6bd11faaa2a%22%2C%22id%22%3A7725978%2C%22hash_user_id%22%3A%2206396acefb7d3e63e11a4b0c3c799a5413bb8704%22%2C%22eid%22%3A%22DXh6undPcFJDtDDli1Ee4g%3D%3D%22%2C%22num_msg%22%3A1%2C%22num_notif%22%3A0%2C%22num_alert%22%3A0%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22Alexey%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3Anull%2C%22receiver_savings_percent%22%3Anull%2C%22receiver_signup%22%3Anull%2C%22referrer_guest%22%3A%221%C2%A0100%E2%82%BD%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3Anull%2C%22offer_discount_type%22%3Anull%7D%7D; _ga=GA1.2.1368901649.1603313680; __ssid=b7712b5193628cb3845c826f88cebb5; _gcl_au=1.1.295923240.1603313700; _uetvid=b255480013df11ebaeab41b2a31101cb; jitney_client_session_id=8dfae4eb-40d8-4881-a391-90e419a5856e; jitney_client_session_created_at=1603905918; jitney_client_session_updated_at=1603907929; _rmt=2--Wzc3MjU5NzgsIjE2fDF8TUxkaXNyTGtERnYxNkN2ciIsIldSemhJcVhZSGN6bGV5Z2NmNWVYd0ZkRjdRbTEtTDRzUVhHMVBXb19vVG8iXQ%3D%3D--c7f9dbe9e1a82377fe764e418d214a26238ba356; _pt=1--WyIwNjM5NmFjZWZiN2QzZTYzZTExYTRiMGMzYzc5OWE1NDEzYmI4NzA0Il0%3D--abaa35e01f086bce54c0f8f654e93a13cdc04f03; _aat=0%7CWGP58ReQru8AqRfNAmyE4H36RNlbetY1hI33SKQyVAupZ0WFwgRPP5LTIKrFqxG%2F; abb_fa2=%7B%22user_id%22%3A%2244%7C1%7CkGlzOmsf2zph4A%2FqeMCp%2BIoKNr6HRo%2FcYeBfglori3BK0nQF1BN%2F%22%7D; rclu=%7B%227725978%22%3D%3E%22bxr3fMfZoLiiZRNFplRGO7DGqyCY4sHQYkW4dD312EM%3D%22%7D; rclmd=%7B%227725978%22%3D%3E%22email%22%7D; cdn_exp_24332663b5ca816ee=control; har=1; previousTab=%7B%22id%22%3A%226186477d-e9d7-4481-8799-9185a9bed306%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.ru%2Finbox%2F876793147%3Fref%3Dredirect-from-messaging-app%26ttype%3Dhome_booking%22%7D; flags=8448; _csrf_token=V4%24.airbnb.ru%24vNJwZHT6B5E%249-b0Gf0vD0ZX7uxtO3OqSIgt72xiPGdr4AOVYw93ceY%3D; auth_jitney_session_id=9111187b-1f52-4cf4-ae36-88a493174f0a; li=1; roles=0; hli=1; __svt=258; cdn_exp_140d70271b981c913=treatment; cdn_exp_283a19eb11edcad71=control
# Pragma: no-cache
# Cache-Control: no-cache
# TE: Trailers'''
    headers = '''Host: www.airbnb.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.airbnb.ru/rooms/34113796?source_impression_id=p3_1667309483_Z8i97TnpzgDmTjYx
X-Airbnb-Supports-Airlock-V2: true
Content-Type: application/json
X-Airbnb-API-Key: d306zoyjsyarp7ifhu67rjxn52tv0t20
X-CSRF-Token: V4$.airbnb.ru$MA23Nay9MNM$QZVNqKnGsrcFdzoFFJo5pfxFMWbHvCcqieRvtih948Q=
X-CSRF-Without-Token: 1
X-Airbnb-GraphQL-Platform: web
X-Airbnb-GraphQL-Platform-Client: minimalist-niobe
X-Niobe-Short-Circuited: true
x-client-request-id: 0b08uq10k44olq0kwowys0dzifnh
DNT: 1
Connection: keep-alive
Cookie: bev=1667309480_YmJlZTI4NGExMjM0; everest_cookie=1667309480.2Dv9LQexEhp9-Qf-Ctno.N7f03T38FxVDnhdOkcmC4x6grIlcjvfY0OXuC5fljTE; _user_attributes=%7B%22curr%22%3A%22USD%22%2C%22guest_exchange%22%3A1.0%2C%22device_profiling_session_id%22%3A%221667309480--26d723f0a03614d41a2f967f%22%2C%22giftcard_profiling_session_id%22%3A%221667309480--10136058b1aae43f25a18cde%22%2C%22reservation_profiling_session_id%22%3A%221667309480--f381c34b1b4512a31643af27%22%7D; _csrf_token=V4%24.airbnb.ru%24MA23Nay9MNM%24QZVNqKnGsrcFdzoFFJo5pfxFMWbHvCcqieRvtih948Q%3D; jitney_client_session_id=1a008405-5c8c-430a-ac60-c4a53df729e1; jitney_client_session_created_at=1667309481; jitney_client_session_updated_at=1667309484; flags=0; previousTab=%7B%22id%22%3A%2258e67ac6-2e70-4b86-bef2-7b65c9ad97aa%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.ru%2Frooms%2F34113796%22%7D; tzo=180; frmfctr=wide
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache
TE: trailers'''

    today = datetime.today()
    extensions = '{"persistedQuery":{"version":1,"sha256Hash":"b94ab2c7e743e30b3d0bc92981a55fff22a05b20bcc9bcc25ca075cc95b42aac"}}'
    variables = '{"request":{"count":12,"listingId":"%(listingId)s","month":%(month)s,"year":%(year)s}}' % dict(listingId=id, month=today.month, year=today.year)
    uri = f'https://www.airbnb.ru/api/v3/PdpAvailabilityCalendar?operationName=PdpAvailabilityCalendar&locale=ru&currency=RUB&variables={variables}&extensions={extensions}&_cb=ssjuv319oa44y'
    r = requests.get(uri, headers=email.message_from_string(headers))
    r.raise_for_status()

    (results_path / f'{id}_raw.json').write_text(r.text)

    items = list(parse(r.text))
    return items



if __name__ == '__main__':
    _parse_place()