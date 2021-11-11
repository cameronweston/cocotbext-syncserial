# HDLC encoded Synchronous Serial interface modules for Cocotb

## Introduction

Synchronous HDLC simulation models for [cocotb](https://GitHub.com/cocotb/cocotb).

## Installation

Installation from respository:

	$ git clone https://github.com/cameronweston/cocotbext-syncserial.git
	$ pip install cocotbext-syncserial

## Documentation and usage examples

See the `tests` directory for a testbench using this module.

### Synchronous Serial

The `SyncSerialSource` and `SyncSerialSink` classes can be used to drive, receive, and monitor HDLC encoded synchronous serial data.

To use these modules, import the module you need and connect it to the DUT.

	from cocotbext.syncserial import SyncSerialSource, SyncSerialSink

	sync_serial_source = SyncSerialSource(dut.data, dut.clk)

	sync_serial_sink = SyncSerialSink(dut.data, dut.clk)

To send data with `SyncSerialSource`, call `write()` or `write_nowait()`. Accepted data types are iterables of 8-bit ints, including lists, bytes, bytearrays, etc.

To receive data with `SyncSerialSink`, call `read()` or `read_nowait()`. `read()` will block until at least 1 packet is available.

#### Constructor parameters:
* _data_: data signal
* _clock_: clock signal
* _clock_rate_mhz_: clock rate in megahertz (optional, default = 10)
* _append_crc_: appends crc to packet (optional, default = True)
* _crc_polynomial_: crc polynomial to use (optional, default = 0x1021)
* _crc_init_: crc initial value to use (optional, default = 0xFFFF)
* _crc_final_xor_: crc final xor to use (optional, default = 0x0000)
* _validate_crc_: validates incoming packet's crc (optional, default = True)
* _strip_crc_: Strips off crc after validation on incoming packet (optional, default = True)

#### Methods
* `write()`: send packet of data (blocking) (source)
* `write_nowait()`: send packet of data (non-blocking) (source)
* `read()`: read one packet of data (blocking) (sink)
* `read_nowait()`: read one packet of data (non-blocking) (sink)
* `count()`: returns the number of packets in the queue (all)
* `empty()`: returns _True_ if the queue is empty (all)
* `clear()`: drop all data from the queue (all)
* `wait(timeout=0, timeout_unit='ns')`: wait for packet received (sink)

### CRC-16

The `Crc_16` classes can be used to calculate or validate a 16 bit CRC. To use this module:
	from cocotbext.syncserial import Crc_16

	crc = Crc_16(crc_polynomial, crc_init, crc_final_xor)

To calculate a CRC, call `calculate_crc()`. Accepted data types are iterables of 8-bit ints, including lists, bytes, bytearrays, etc.

To validate a CRC, call `validate_crc()`. Accepted data types are iterables of 8-bit ints, including lists, bytes, bytearrays, etc.

#### Constructor parameters:
* _crc_polynomial_: CRC polynomial to use (optional, default = 0x1021)
* _crc_init_: CRC initial value to use (optional, default = 0xFFFF)
* _crc_final_xor_: CRC final XOR value to use (optional, default = 0x0000)

#### Methods
* `validate_crc(data, crc)`: Calculates a CRC for data and compared to crc
* `calculate_crc(data)`: Calucalates and returns a CRC for data