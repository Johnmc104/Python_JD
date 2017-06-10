# -*- coding: utf-8 -*-

import requests
requests.post(
    "https://api.alertover.com/v1/alert",
    data={
        "source": "s-82e569ef-57b9-4bd6-ab23-b2099031",
        "receiver": "g-259d7e81-df26-48a2-aa91-60d0dced",
        "content": "Test2",
        "title": "风云气象站"
    }
)
