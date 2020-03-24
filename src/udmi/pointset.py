"""
{
  "title": "Pointset telemetry schema",
  "type": "object",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "additionalProperties": false,
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "version": {
      "enum": [
        1
      ]
    },
    "points": {
      "additionalProperties": false,
      "patternProperties": {
        "^[a-z][a-z0-9]*(_[a-z0-9]+)*$": {
          "$ref": "#/definitions/point_property_names"
        }
      }
    }
  },
  "required": [
    "timestamp",
    "version",
    "points"
  ],
  "definitions": {
    "point_property_names": {
      "type": "object",
      "propertyNames": {
        "oneOf": [
          {
            "enum": [
              "present_value"
            ]
          }
        ]
      },
      "required": [
        "present_value"
      ]
    }
  }
}
"""

from .base import UDMIBase, DEFAULT_UDMI_VERSION


class Pointset(UDMIBase):

    schema = "pointset.json"
    __slots__ = ["version", "version", "timestamp", "points"]

    def __init__(self, timestamp, points, version=DEFAULT_UDMI_VERSION):

        self.timestamp = self.serialise_timestamp(timestamp)
        self.points = points
        super().__init__(version)
