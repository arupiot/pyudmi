import unittest
import datetime
from fastjsonschema import JsonSchemaException

from udmi.config import Config
from udmi.discovery import Discovery
from udmi.logentry import LogEntry
from udmi.metadata import MetaData
from udmi.pointset import Pointset
from udmi.properties import Properties
from udmi.state import State


class TestCreateTopLevelObjects(unittest.TestCase):

    def test_create_config(self):
        timestamp = datetime.datetime.utcnow()
        system = {
            "min_loglevel": 500
        }
        gateway = {
            "devices": {
                "AHU-123": {
                    "protocol": "bacnet",
                    "local_id": "327412"
                }
            },
            "scan_interval_sec": 10
        }
        pointset = {
            "sample_limit_sec": 2,
            "sample_rate_sec": 500,
            "points": {
                "return_air_temperature_sensor": {
                    "force_value": 21.1
                }
            }
        }

        config1 = Config(timestamp, system, pointset, gateway)
        # check without the optional bits
        _ = Config(timestamp, system)
        # check fails
        self.assertRaises(JsonSchemaException, Config, timestamp, None)
        # try round trip
        udmi = str(config1)
        remade = Config.from_string(udmi)
        self.assertEqual(config1.as_dict(), remade.as_dict())

    def test_create_discovery(self):
        timestamp = datetime.datetime.utcnow()
        protocol = "bacnet"
        local_id = "92EA09"
        points = {
            "reading_value": {
                "units": "C",
                "present_value": 21.30108642578125
            }
        }

        discovery = Discovery(timestamp, protocol, local_id, points)

        # try round trip
        udmi = str(discovery)
        remade = Discovery.from_string(udmi)
        self.assertEqual(discovery.as_dict(), remade.as_dict())

    def test_create_logentry(self):
        timestamp = datetime.datetime.utcnow()
        entries = [
            {
                "message": "things are happening",
                "detail": "someplace, sometime",
                "timestamp": "2018-08-26T21:39:19.364Z",
                "category": "com.testCategory",
                "level": 600
            },
            {
                "message": "something else happened",
                "timestamp": "2018-08-26T21:39:39.364Z",
                "detail": "someplace, sometime",
                "category": "com.testCategory",
                "level": 700
            }
        ]

        log_entry = LogEntry(timestamp, entries)

        # try round trip
        udmi = str(log_entry)
        remade = LogEntry.from_string(udmi)
        self.assertEqual(log_entry.as_dict(), remade.as_dict())

    def test_create_metadata(self):
        timestamp = datetime.datetime.utcnow()
        system = {
            "location": {
                "site_name": "US-SFO-XYY",
                "section": "NW-2F",
                "position": {
                    "x": 10,
                    "y": 20
                }
            },
            "physical_tag": {
                "asset": {
                    "guid": "bim://04aEp5ymD_$u5IxhJN2aGi",
                    "name": "US-SFO-XYY_AHU-1_extention11-optional"
                }
            }
        }
        hash = "12345678"
        gateway = {
            "gateway_id": "GAT-12",
            "protocol": "bacnet",
            "local_id": "*82AE98"
        }

        pointset = {
            "points": {
                "return_air_temperature_sensor": {
                    "units": "Degrees-Celsius"
                }
            }
        }

        meta_data = MetaData(timestamp, system, hash=hash, gateway=gateway, pointset=pointset)

        # try round trip
        udmi = str(meta_data)
        remade = MetaData.from_string(udmi)
        self.assertEqual(meta_data.as_dict(), remade.as_dict())
        _meta_data = MetaData(timestamp, system)

    def test_create_pointset(self):
        timestamp = datetime.datetime.utcnow()
        points = {
            "reading_value": {
                "present_value": 21.30108642578125
            },
            "yoyo_motion_sensor": {
                "present_value": True
            },
            "enum_value": {
                "present_value": "hello"
            }
        }

        pointset = Pointset(timestamp, points)
        # try round trip
        udmi = str(pointset)
        remade = Pointset.from_string(udmi)
        self.assertEqual(pointset.as_dict(), remade.as_dict())

        self.assertRaises(JsonSchemaException, Pointset, timestamp, None)

    def test_create_properties(self):

        key_type = "RSA_PEM"
        connect = "direct"

        properties = Properties(key_type, connect)

        # try round trip
        udmi = str(properties)
        remade = Properties.from_string(udmi)
        self.assertEqual(properties.as_dict(), remade.as_dict())

    def test_create_state(self):
        timestamp = datetime.datetime.utcnow()
        system = {
            "make_model": "ACME Bird Trap",
            "firmware": {
                "version": "3.2a"
            }
        }

        state = State(timestamp, system, pointset=None)

        # try round trip
        udmi = str(state)
        remade = State.from_string(udmi)
        self.assertEqual(state.as_dict(), remade.as_dict())
