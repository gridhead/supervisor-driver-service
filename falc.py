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

import click
import falcon
from base.frnt import (
    ConnectionManager,
    ProcessControllingEndpoint,
    ProcessHandlingEndpoint,
    StatisticalEndpoint,
)
from falcon import __version__ as flcnvers
from psutil import __version__ as psutvers
from werkzeug import __version__ as wkzgvers
from docker import __version__ as dockvers
from werkzeug import serving


main = falcon.API()


@click.command()
@click.option("-p", "--portdata", "portdata", help="Set the port value [0-65536].", default="6969")
@click.option("-6", "--ipprotv6", "netprotc", flag_value="ipprotv6", help="Start the server on an IPv6 address.")
@click.option("-4", "--ipprotv4", "netprotc", flag_value="ipprotv4", help="Start the server on an IPv4 address.")
@click.version_option(version="1.0.2", prog_name=click.style("SuperVisor Driver Service", fg="magenta"))
def mainfunc(portdata, netprotc):
    try:
        click.echo(" * " + click.style("SuperVisor Driver Service v1.0.2", fg="green"))
        netpdata = ""
        passcode = ConnectionManager().passphrase_generator()
        if netprotc == "ipprotv6":
            click.echo(" * " + click.style("IP version        ", fg="magenta") + ": " + "6")
            netpdata = "::"
        elif netprotc == "ipprotv4":
            click.echo(" * " + click.style("IP version        ", fg="magenta") + ": " + "4")
            netpdata = "0.0.0.0"
        click.echo(" * " + click.style("Passcode          ", fg="magenta") + ": " + passcode + "\n" +
                   " * " + click.style("Reference URI     ", fg="magenta") + ": " + "http://" + netpdata + ":" + portdata +
                   "/" + "\n" +
                   " * " + click.style("Monitor service   ", fg="magenta") + ": " + "DockerPy v" + dockvers + "\n" +
                   " * " + click.style("Container service ", fg="magenta") + ": " + "Psutil v" + psutvers + "\n" +
                   " * " + click.style("Endpoint service  ", fg="magenta") + ": " + "Falcon v" + flcnvers + "\n" +
                   " * " + click.style("HTTP server       ", fg="magenta") + ": " + "Werkzeug v" + wkzgvers)
        statsync = StatisticalEndpoint(passcode)
        procinfo = ProcessHandlingEndpoint(passcode)
        proctool = ProcessControllingEndpoint(passcode)
        main.add_route("/statsync", statsync)
        main.add_route("/procinfo", procinfo)
        main.add_route("/proctool", proctool)
        serving.run_simple(netpdata, int(portdata), main)
    except Exception as expt:
        click.echo(" * " + click.style("Error occurred    : " + str(expt), fg="red"))


if __name__ == "__main__":
    mainfunc()
