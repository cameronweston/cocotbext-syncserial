# HDLC encoded Synchronous Serial interface modules for Cocotb

## Introduction

Synchronous HDLC simulation models for [cocotb](https://GitHub.com/cocotb/cocotb).

## Installation

Installation from respository: 
	
	$ git clone https://github.com/cameronweston/cocotbext-syncserial.git
	$ pip install -e cocotbext-hdlc

## Documentation and usage examples

See the `tests` directory for a testbench using this module.

### Synchronous Serial

The `SyncSerialSource` and `SyncSerialSink` classes can be used to drive, receive, and monitor HDLC encoded synchronous serial data.

To use these modules, import the module you need and connect it to the DUT. 

	from cocotbext.syncserial import SyncSerialSource, SyncSerialSink
	
	sync_serial_source = TBD

	sync_serial_sink = TBD

To send data with `SyncSerialSource`, TBD

To receive data with `SyncSerialSink`, TBD

#### Constructor parameters:
TBD

#### Methods