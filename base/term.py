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

import tornado.ioloop
import tornado.web
from terminado import TermSocket, UniqueTermManager


def inptloop(termmngr):
    loop = tornado.ioloop.IOLoop.instance()
    try:
        loop.start()
    except KeyboardInterrupt:
        print("\nShutting down on SIGINT")
    finally:
        termmngr.shutdown()
        loop.close()


def mainterm(portqant):
    termmngr = UniqueTermManager(shell_command=["sh"])
    handlers = [
        (
            r"/websocket", TermSocket,
            {
                'term_manager': termmngr
            }
        )
    ]
    mainobjc = tornado.web.Application(handlers)
    print(" * TermSocket started on port " + portqant)
    mainobjc.listen(portqant, "0.0.0.0")
    inptloop(termmngr)
