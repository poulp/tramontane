# coding: utf-8

import signal

from tramontane.app import TramontaneApp

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = TramontaneApp()
    app.run()