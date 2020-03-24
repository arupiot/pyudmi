"""
{
  "title": "Log entry schema",
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
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/report"
      }
    }
  },
  "required": [
    "entries",
    "timestamp",
    "version"
  ],
  "definitions": {
    "report": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "message": {
          "type": "string"
        },
        "detail": {
          "type": "string"
        },
        "category": {
          "type": "string",
          "pattern": "^[a-z][.a-zA-Z]*[a-zA-Z]$"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "level": {
          "$comment": "https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity",
          "type": "integer",
          "multipleOf": 1,
          "minimum": 100,
          "maximum": 800
        }
      },
      "required": [
        "message",
        "category",
        "timestamp",
        "level"
      ]
    }
  }
}

"""

from .base import UDMIBase, DEFAULT_UDMI_VERSION


class LogEntry(UDMIBase):

    schema = "logentry.json"
    __slots__ = ["version", "timestamp", "entries"]

    def __init__(self, timestamp, entries, version=DEFAULT_UDMI_VERSION):

        self.timestamp = self.serialise_timestamp(timestamp)
        self.entries = entries
        super().__init__(version)
