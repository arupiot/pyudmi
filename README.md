# UDMI Python helpers

## Intro

This is a set of classes to help when working with UDMI. See https://github.com/faucetsdn/daq/blob/master/schemas/udmi/README.md

There are currently seven classes representing the corresponding UDMI types:

- Config
- Discovery
- LogEntry
- MetaData
- Pointset
- Properties
- State

They are available at the top level of this module. ie udmi.Pointset

So far the subtypes used in UDMI such as config_pointest are not representated by classes and remain dicts

They do three useful things currently:

### Validation

They perform data validation against the published version 1 UDMI json schemas on creation, throwing an exception if the input data is malformed.

### Serialisation

Uniform serialisation to the udmi json format from object orientated interface.

### Timestamps

There's a method that serialises timestamps given in python datetime format correctly.

## Installation

```python
pip install pyudmi
```

## Usage

You can create these objects in two ways. Each class has a normal Python constructor to make programatic creation easier eg:

```python
import udmi

config = udmi.Config(timestamp, system, pointset, gateway)
```
 
And a class method common to them all:

```python

config = udmi.Config.from_string(udmi_string)
```

To serialise as a udmi json string use the method `as_udmi`

```python

udmi_string = config.as_udmi()
```