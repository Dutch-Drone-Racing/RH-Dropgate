from eventmanager import Evt
from .dropgate import Dropgate


def initialize(rhapi):
    dropgate = Dropgate(rhapi)
    rhapi.events.on(Evt.STARTUP, dropgate.init_plugin)

    rhapi.events.on(Evt.RACE_START, dropgate.trigger_drop)
    rhapi.events.on(Evt.RACE_STOP, dropgate.reactivate_drop)
