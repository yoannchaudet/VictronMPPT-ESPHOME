import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import ICON_EMPTY

from . import CONF_VICTRON_ID, VictronComponent

DEPENDENCIES = ["victron"]

CODEOWNERS = ["@KinDR007"]

CONF_LOAD_STATE = "load_state"
CONF_RELAY_STATE = "relay_state"

BINARY_SENSORS = [
    CONF_LOAD_STATE,
    CONF_RELAY_STATE,
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_VICTRON_ID): cv.use_id(VictronComponent),
        cv.Optional(CONF_LOAD_STATE): binary_sensor.binary_sensor_schema(
            icon=ICON_EMPTY
        ),
        cv.Optional(CONF_RELAY_STATE): binary_sensor.binary_sensor_schema(
            icon=ICON_EMPTY
        ),
    }
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_VICTRON_ID])
    for key in BINARY_SENSORS:
        if key in config:
            conf = config[key]
            sens = await binary_sensor.new_binary_sensor(conf)
            cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))
