"""
##########################################################################
*
*   Copyright © 2019-2021 Akashdeep Dhar <t0xic0der@fedoraproject.org>
*
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <https://www.gnu.org/licenses/>.
*
##########################################################################
"""

import json
from hashlib import sha256
from os import system
from sys import exit
from time import ctime, sleep, time

import falcon
from base.back import LiveUpdatingElements
from click import echo
from redis import Redis


class RedisDatastoreServerSetup():
    def __init__(self, portnumb, protmode):
        self.portnumb = str(portnumb)
        if protmode:
            self.protmode = "yes"
        else:
            self.protmode = "no"

    def execute_redis_server_process(self):
        """
        Starting a local Redis datastore server at port 6379 and disabled protected mode
        """
        try:
            echo(" * Starting Redis datastore server...")
            system("redis-server --port " + self.portnumb + " --protected-mode " + self.protmode)
        except KeyboardInterrupt:
            echo("\n" + " * Stopped Redis datastore server...")
            exit()


class MetricsRetrievingEndpoint(object):
    def __init__(self, passcode, duration, recsqant):
        """
        Initialize storage connection
        """
        self.baseobjc = Redis(host="127.0.0.1", port=6379)
        self.passcode = passcode
        self.duration = duration
        self.recsqant = recsqant

    def on_get(self, rqst, resp):
        """
        Endpoint for retrieving metrics
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        mtrciden = rqst.get_param("mtrciden")
        if passcode == self.passcode:
            try:
                if opername == "LIST":
                    mtrckeys = [indx.decode() for indx in self.baseobjc.keys()]
                    mtrckeys.sort()
                    retnjson = {
                        "duration": self.duration,
                        "recsqant": self.recsqant,
                        "mtrclist": mtrckeys
                    }
                elif opername == "IDEN":
                    mtrciden = str(mtrciden).encode()
                    retnjson = json.loads(self.baseobjc.get(mtrciden))
                else:
                    retnjson = {"retnmesg": "deny"}
            except Exception:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class GatherMetricToStorage(object):
    def __init__(self, duration, recsqant):
        """
        Initialize storage connection
        """
        echo(" * Initializing metric fetch system...")
        self.baseobjc = Redis(host="127.0.0.1", port=6379)
        self.duration = duration
        self.recsqant = recsqant

    def jsonify_system_live_updating_metrics(self):
        """
        Convert metric data to a JSON-friendly format
        """
        timestmp = str(time()).split(".")[0]
        hashiden = sha256(timestmp.encode()).hexdigest()
        keyvalpr = {
            timestmp: json.dumps({
                "hashiden": hashiden,
                "liveupdt": LiveUpdatingElements().return_live_data()
            })
        }
        return keyvalpr

    def continuously_store_data(self):
        """
        Periodically push passive metrics to Redis store
        """
        self.baseobjc.flushall()
        try:
            while True:
                if self.baseobjc.dbsize() == self.recsqant:
                    self.baseobjc.keys().sort()
                    self.baseobjc.delete(self.baseobjc.keys()[0])
                self.baseobjc.mset(self.jsonify_system_live_updating_metrics())
                echo(" * [" + ctime() + "] Stored system metrics now...")
                sleep(self.duration)
        except KeyboardInterrupt as expt:
            self.baseobjc.close()
            echo("\n" + " * Closing storage connection...")
            exit()
