# Synchronous HDLC interface modules for Cocotb

## Introduction

Synchronous HDLC simulation models for [cocotb] (https://GitHub.com/cocotb/cocotb).

## Installation

Installation from respository: 
	
	$ git clone TBD
	$ pip install -e cocotbext-hdlc

## Documentation and usage examples

See the `tests` directory for a testbench using this module.

### HDLC

The `HdlcSource` and `HdlcSink` classes can be used to drive, receive, and monitor HDLC data.

To use these modules, import the module you need and connect it to the DUT. 

	from cocotbext.hdlc import HdlcSource, HdlcSink
	
	hdlc_source = TBD

	hdlc_sink = TBD

To send data with `HdlcSource`, TBD

To receive data with `HdlcSink`, TBD

#### Constructor parameters:
TBD

#### Methods