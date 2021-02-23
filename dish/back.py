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

from docker import DockerClient


class DockerPreliminaryInformation:
    def __init__(self, unixsock):
        self.clinobjc = DockerClient(base_url=unixsock)

    def get_docker_info(self):
        """
        Returns container station information
        """
        return self.clinobjc.info()

    def get_docker_version(self):
        """
        Returns container station versioning
        """
        return self.clinobjc.version()


class DockerContainerInformation:
    def __init__(self, unixsock):
        self.clinobjc = DockerClient(base_url=unixsock)

    def get_container_list(self):
        """
        Returns list of containers
        """
        contlist = self.clinobjc.containers.list(all=True)
        dispdict = {}
        for indx in contlist:
            dispdict[indx.short_id] = {
                "id": indx.id,
                "name": indx.name,
            }
        return dispdict

    def get_per_container_static_information(self, contiden):
        """
        Returns preliminary information of a selected container
        """
        try:
            contobjc = self.clinobjc.containers.get(contiden)
            try:
                imejname = contobjc.image.tags[0]
            except:
                imejname = "UNAVAILABLE"
            dispdict = {
                "short_id": contobjc.short_id,
                "id": contobjc.id,
                "name": contobjc.name,
                "attrs": contobjc.attrs,
                "labels": contobjc.labels,
                "ports": contobjc.ports,
                "status": contobjc.status,
                "image": {
                    "name": imejname,
                    "short_id": contobjc.image.short_id
                }
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict

    def get_per_container_logs_data(self, contiden):
        """
        Returns logging information of a selected container
        """
        try:
            contobjc = self.clinobjc.containers.get(contiden)
            dispdict = {
                "logs": contobjc.logs(stream=False).decode()
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict

    def get_per_container_top_data(self, contiden):
        """
        Returns list of processes running in a selected container
        """
        try:
            contobjc = self.clinobjc.containers.get(contiden)
            dispdict = {
                "top": contobjc.top()
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict

    def get_per_container_statistics(self, contiden):
        """
        Returns hardware statistics of a selected container
        """
        try:
            contobjc = self.clinobjc.containers.get(contiden)
            dispdict = {
                "stats": contobjc.stats(stream=False)
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict


class DockerImageInformation:
    def __init__(self, unixsock):
        self.clinobjc = DockerClient(base_url=unixsock)

    def get_image_list(self):
        """
        Returns list of images
        """
        imejlist = self.clinobjc.images.list(all=True)
        dispdict = {}
        for indx in imejlist:
            try:
                imejname = indx.tags[0]
            except:
                imejname = "UNAVAILABLE"
            dispdict[indx.short_id] = {
                "id": indx.id,
                "name": imejname,
            }
        return dispdict

    def get_per_image_static_information(self, imejiden):
        """
        Returns preliminary information of a selected image
        """
        try:
            imejobjc = self.clinobjc.images.get(imejiden)
            try:
                imejname = imejobjc.tags[0]
            except:
                imejname = "UNAVAILABLE"
            dispdict = {
                "short_id": imejobjc.short_id,
                "id": imejobjc.id,
                "name": imejname,
                "attrs": imejobjc.attrs,
                "labels": imejobjc.labels,
                "tags": imejobjc.tags
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict

    def get_per_image_revision_history(self, imejiden):
        """
        Returns revision history of a selected container
        """
        try:
            imejobjc = self.clinobjc.images.get(imejiden)
            dispdict = {
                "history": imejobjc.history()
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict


class DockerNetworkInformation:
    def __init__(self, unixsock):
        self.clinobjc = DockerClient(base_url=unixsock)

    def get_network_list(self):
        """
        Returns list of networks
        """
        ntwklist = self.clinobjc.networks.list()
        dispdict = {}
        for indx in ntwklist:
            dispdict[indx.short_id] = {
                "id": indx.id,
                "name": indx.name,
            }
        return dispdict

    def get_per_network_static_information(self, ntwkiden):
        """
        Returns preliminary information of a selected network
        """
        try:
            ntwkobjc = self.clinobjc.networks.get(ntwkiden)
            dispdict = {
                "short_id": ntwkobjc.short_id,
                "id": ntwkobjc.id,
                "name": ntwkobjc.name,
                "attrs": ntwkobjc.attrs
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict


class DockerVolumeInformation:
    def __init__(self, unixsock):
        self.clinobjc = DockerClient(base_url=unixsock)

    def get_volume_list(self):
        """
        Returns list of volumes
        """
        volmlist = self.clinobjc.volumes.list()
        dispdict = {}
        for indx in volmlist:
            dispdict[indx.short_id] = {
                "id": indx.id,
                "name": indx.name,
            }
        return dispdict

    def get_per_volume_static_information(self, volmiden):
        """
        Returns preliminary information of a selected volume
        """
        try:
            volmobjc = self.clinobjc.volumes.get(volmiden)
            dispdict = {
                "short_id": volmobjc.short_id,
                "id": volmobjc.id,
                "name": volmobjc.name,
                "attrs": volmobjc.attrs
            }
        except:
            dispdict = {
                "retnmesg": "deny"
            }
        return dispdict
