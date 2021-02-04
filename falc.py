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
from secrets import choice

import click
import falcon
from base.frnt import (
    ProcessControllingEndpoint,
    ProcessHandlingEndpoint,
    StatisticalEndpoint,
)
from dish.frnt import (
    ContainerInformationEndpoint,
    ImageInformationEndpoint,
    NetworkInformationEndpoint,
    PreliminaryInformationEndpoint,
    VolumeInformationEndpoint,
)
from docker import __version__ as dockvers
from falcon import __version__ as flcnvers
from psutil import __version__ as psutvers
from werkzeug import __version__ as wkzgvers
from werkzeug import serving


main = falcon.API()


class ConnectionManager:
    def passphrase_generator(self, lent=16):
        retndata = "".join(choice("ABCDEF0123456789") for indx in range(lent))
        return retndata


class ConnectionExaminationEndpoint(object):
    def __init__(self, passcode):
        self.passcode = passcode

    def on_get(self, rqst, resp):
        passcode = rqst.get_param("passcode")
        if passcode == self.passcode:
            retnjson = {"retnmesg": "allow"}
        else:
            retnjson = {"retnmesg": "deny"}
        resp.body = json.dumps(retnjson, ensure_ascii=False)
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.status = falcon.HTTP_200


@click.command()
@click.option(
    "-p",
    "--portdata",
    "portdata",
    help="Set the port value [0-65536].",
    default="6969"
)
@click.option(
    "-u",
    "--unixsock",
    "unixsock",
    help="Set the UNIX socket for Docker.",
    default="unix://var/run/docker.sock"
)
@click.option(
    "-6",
    "--ipprotv6",
    "netprotc",
    flag_value="ipprotv6",
    help="Start the server on an IPv6 address."
)
@click.option(
    "-4",
    "--ipprotv4",
    "netprotc",
    flag_value="ipprotv4",
    help="Start the server on an IPv4 address."
)
@click.version_option(
    version="1.1.0-beta",
    prog_name=click.style("SuperVisor Driver Service", fg="magenta")
)
def mainfunc(portdata, netprotc, unixsock):
    try:
        click.echo(
            click.style(
                " ,---.                    .    ,o               \n" +
                " `---..   .,---.,---.,---.|    |.,---.,---.,---.\n" +
                "     ||   ||   ||---'|     \  / |`---.|   ||    \n" +
                " `---'`---'|---'`---'`      `'  ``---'`---'`    \n" +
                "           |", bold=True
            )
        )
        click.echo(" * " + click.style("Driver Service v1.1.0-beta", fg="green"))
        netpdata = ""
        passcode = ConnectionManager().passphrase_generator()
        if netprotc == "ipprotv6":
            click.echo(" * " + click.style("IP version        ", fg="magenta") + ": " + "6")
            netpdata = "::"
        elif netprotc == "ipprotv4":
            click.echo(" * " + click.style("IP version        ", fg="magenta") + ": " + "4")
            netpdata = "0.0.0.0"
        click.echo(
            " * " + click.style("Passcode          ", bold=True) + ": " + passcode + "\n" +
            " * " + click.style("Reference URI     ", bold=True) + ": " + "http://" + netpdata + ":" + portdata +
            "/" + "\n" +
            " * " + click.style("Monitor service   ", bold=True) + ": " + "Psutil v" + psutvers + "\n" +
            " * " + click.style("Container service ", bold=True) + ": " + "DockerPy v" + dockvers + "\n" +
            " * " + click.style("Endpoint service  ", bold=True) + ": " + "Falcon v" + flcnvers + "\n" +
            " * " + click.style("HTTP server       ", bold=True) + ": " + "Werkzeug v" + wkzgvers
        )
        basestat = StatisticalEndpoint(passcode)
        basepsin = ProcessHandlingEndpoint(passcode)
        basetool = ProcessControllingEndpoint(passcode)
        dishplim = PreliminaryInformationEndpoint(passcode, unixsock)
        dishcont = ContainerInformationEndpoint(passcode, unixsock)
        dishimej = ImageInformationEndpoint(passcode, unixsock)
        dishntwk = NetworkInformationEndpoint(passcode, unixsock)
        dishvolm = VolumeInformationEndpoint(passcode, unixsock)
        testconn = ConnectionExaminationEndpoint(passcode)
        main.add_route("/basestat", basestat)
        main.add_route("/basepsin", basepsin)
        main.add_route("/basetool", basetool)
        main.add_route("/dishplim", dishplim)
        main.add_route("/dishcont", dishcont)
        main.add_route("/dishimej", dishimej)
        main.add_route("/dishntwk", dishntwk)
        main.add_route("/dishvolm", dishvolm)
        main.add_route("/testconn", testconn)
        serving.run_simple(netpdata, int(portdata), main)
    except Exception as expt:
        click.echo(" * " + click.style("Error occurred    : " + str(expt), fg="red"))


if __name__ == "__main__":
    mainfunc()
