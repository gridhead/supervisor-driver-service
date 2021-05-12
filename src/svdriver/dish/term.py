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

from tornado.ioloop import IOLoop
import tornado.web
from terminado import TermSocket, UniqueTermManager
import sys
from hashlib import sha256
from click import echo


class AttachmentEndpoint(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def get(self):
        try:
            contiden = self.get_argument("contiden")
            comdexec = self.get_argument("comdexec")
            self.write(addhandr(contiden, comdexec))
        except Exception as expt:
            echo(" * Console attachment failed! - " + str(expt))
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({"retnmesg": "deny"})


termmngr = UniqueTermManager(shell_command=["sh"])


handlers = [
    (
        r"/websocket", TermSocket,
        {
            "term_manager": termmngr
        }
    ),
    (
        r"/atchcons/", AttachmentEndpoint
    )
]


def mainterm(portqant):
    try:
        global mainobjc
        mainobjc = tornado.web.Application(handlers)
        echo(" * TermSocket started on port " + portqant)
        mainobjc.listen(portqant, "0.0.0.0")
        IOLoop.instance().start()
    except KeyboardInterrupt:
        echo("\n" + " * Shutting down on SIGINT")
    finally:
        sys.exit()


def addhandr(contiden, comdexec):
    try:
        echo(" * " + comdexec + " attached to " + contiden)
        urlpatrn = sha256((contiden + comdexec).encode()).hexdigest()
        comdexec = comdexec.split()
        stndexec = ["docker", "exec", "-ti", contiden]
        for indx in comdexec:
            stndexec.append(indx)
        mainobjc.add_handlers(
            r".*",  # match any host
            [
                (
                    r"/" + urlpatrn, TermSocket,
                    {
                        "term_manager": UniqueTermManager(shell_command=stndexec)
                    }
                )
            ]
        )
        return {
            "retnmesg": "allow",
            "urlpatrn": urlpatrn
        }
    except Exception as expt:
        echo(" * Failed to attach terminal" + "\n" + str(expt))
        return {
            "retnmesg": "deny"
        }
