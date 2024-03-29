
"""
{
  "title": "Device metadata schema",
  "type": "object",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "additionalProperties": false,
  "required": [
    "timestamp",
    "version",
    "system"
  ],
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
    "hash": {
      "type": "string",
      "pattern": "^[0-9a-z]{8}$"
    },
    "system": {
      "$ref": "file:metadata_system.json#"
    },
    "gateway": {
      "$ref": "file:metadata_gateway.json#"
    },
    "pointset": {
      "$ref": "file:metadata_pointset.json#"
    }
  }
}
"""


from .base import UDMIBase, DEFAULT_UDMI_VERSION


class MetaData(UDMIBase):

    schema = "metadata.json"
    __slots__ = ["version", "timestamp", "system", "hash", "gateway", "pointset", "cloud"]

    def __init__(self, timestamp, system, hash=None, gateway=None, pointset=None, cloud=None, version=DEFAULT_UDMI_VERSION):

        self.timestamp = self.serialise_timestamp(timestamp)
        self.pointset = pointset
        self.gateway = gateway
        self.system = system
        self.hash = hash
        self.cloud = cloud
        super().__init__(version)
