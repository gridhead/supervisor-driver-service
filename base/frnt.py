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

import falcon
from base.back import DeadUpdatingElements, LiveUpdatingElements, ProcessHandler


class StatisticalEndpoint(object):
    def __init__(self, passcode):
        self.passcode = passcode

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching host station information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "livesync":
                retnjson = LiveUpdatingElements().return_live_data()
            elif opername == "deadsync":
                retnjson = DeadUpdatingElements().return_dead_data()
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class ProcessHandlingEndpoint(object):
    def __init__(self, passcode):
        self.passcode = passcode

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching information about a specific process
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        if passcode == self.passcode:
            retnjson = ProcessHandler(int(rqst.get_param("prociden"))).return_process_info()
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class ProcessControllingEndpoint(object):
    def __init__(self, passcode):
        self.passcode = passcode

    def on_get(self, rqst, resp):
        """
        Endpoint for controlling specific processes
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        prociden = int(rqst.get_param("prociden"))
        if passcode == self.passcode:
            if opername == "KILL":
                retnjson = ProcessHandler(prociden).process_killer()
            elif opername == "TERM":
                retnjson = ProcessHandler(prociden).process_terminator()
            elif opername == "HANG":
                retnjson = ProcessHandler(prociden).process_suspender()
            elif opername == "CONT":
                retnjson = ProcessHandler(prociden).process_resumer()
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200
