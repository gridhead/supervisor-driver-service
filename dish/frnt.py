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
from dish.back import (
    DockerPreliminaryInformation,
    DockerContainerInformation,
    DockerImageInformation,
    DockerNetworkInformation,
    DockerVolumeInformation
)


class PreliminaryInformationEndpoint(object):
    def __init__(self, passcode, unixsock):
        self.passcode = passcode
        self.unixsock = unixsock

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching container station information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "INFO":
                retnjson = DockerPreliminaryInformation(self.unixsock).get_docker_info()
            elif opername == "VERS":
                retnjson = DockerPreliminaryInformation(self.unixsock).get_docker_version()
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class ContainerInformationEndpoint(object):
    def __init__(self, passcode, unixsock):
        self.passcode = passcode
        self.unixsock = unixsock

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching container information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "LIST":
                retnjson = DockerContainerInformation(self.unixsock).get_container_list()
            elif opername == "IDEN":
                contiden = rqst.get_param("contiden")
                retnjson = DockerContainerInformation(self.unixsock).get_per_container_static_information(contiden)
            elif opername == "LOGS":
                contiden = rqst.get_param("contiden")
                retnjson = DockerContainerInformation(self.unixsock).get_per_container_logs_data(contiden)
            elif opername == "HTOP":
                contiden = rqst.get_param("contiden")
                retnjson = DockerContainerInformation(self.unixsock).get_per_container_top_data(contiden)
            elif opername == "STAT":
                contiden = rqst.get_param("contiden")
                retnjson = DockerContainerInformation(self.unixsock).get_per_container_statistics(contiden)
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class ImageInformationEndpoint(object):
    def __init__(self, passcode, unixsock):
        self.passcode = passcode
        self.unixsock = unixsock

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching image information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "LIST":
                retnjson = DockerImageInformation(self.unixsock).get_image_list()
            elif opername == "IDEN":
                imejiden = rqst.get_param("imejiden")
                retnjson = DockerImageInformation(self.unixsock).get_per_image_static_information(imejiden)
            elif opername == "REVS":
                imejiden = rqst.get_param("imejiden")
                retnjson = DockerImageInformation(self.unixsock).get_per_image_revision_history(imejiden)
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class NetworkInformationEndpoint(object):
    def __init__(self, passcode, unixsock):
        self.passcode = passcode
        self.unixsock = unixsock

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching network information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "LIST":
                retnjson = DockerNetworkInformation(self.unixsock).get_network_list()
            elif opername == "IDEN":
                ntwkiden = rqst.get_param("ntwkiden")
                retnjson = DockerNetworkInformation(self.unixsock).get_per_network_static_information(ntwkiden)
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


class VolumeInformationEndpoint(object):
    def __init__(self, passcode, unixsock):
        self.passcode = passcode
        self.unixsock = unixsock

    def on_get(self, rqst, resp):
        """
        Endpoint for fetching volume information
        Method: GET
        """
        passcode = rqst.get_param("passcode")
        opername = rqst.get_param("opername")
        if passcode == self.passcode:
            if opername == "LIST":
                retnjson = DockerVolumeInformation(self.unixsock).get_volume_list()
            elif opername == "IDEN":
                volmiden = rqst.get_param("volmiden")
                retnjson = DockerVolumeInformation(self.unixsock).get_per_volume_static_information(volmiden)
            else:
                retnjson = {"retnmesg": "deny"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200
