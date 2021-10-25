"""

Some copyright

"""

import logging
from collections import deque

import cocotb
from cocotb.triggers import FallingEdge, RisingEdge
from cocotb.clock import Clock

from .version import __version__

class SyncSerialSource:
    def __init__(self, data, clock, clock_rate_mhz = 10, append_crc = True, crc_polynomial = 0x1021, crc_init = 0xFFFF, *args, **kwargs):
        self.log = logging.getLogger(f"cocotb.{data._path}")
        self._data = data
        self._clock = clock
        self._clock_rate_mhz = clock_rate_mhz
        self._append_crc = append_crc
        self._crc_polynomial = crc_polynomial
        self._crc_init = crc_init
        
        self.log.info("HDLC source")
        self.log.info("cocotbext-hdlc version %s", __version__)
        self.log.info("Copyright (c) 2021 Cameron Weston")
        self.log.info("https://github.com/TBD/cocotbext-hdlc")
        
        super().__init__(*args, **kwargs)
        
        self.queue = deque()
        
        self._data.setimmediatevalue(0)
        self._clock.setimmediatevalue(0)
        
        self.log.info("HDLC source configuration:")
        self.log.info(" Clock Rate: %f Mhz", self._clock_rate_mhz)
        self.log.info(" Append CRC: %s", self._append_crc)
        if self._append_crc == True:
            self.log.info(" Initial Value: %s", hex(self._crc_init))
            self.log.info(" CRC Polynomial: %s", hex(self._crc_polynomial))
        
        self._data_cr = None
        self._clk_cr = None
        self._restart()
        
    def _restart(self):
        if self._data_cr is not None:
            self._data_cr.kill()
        if self._clk_cr is not None:
            self._clk_cr.kill()
            
        # Start the data and clock coroutines
        self._data_cr = cocotb.start_soon(self._run().start())
        self._clk_cr = cocotb.start_soon(Clock(self._clock, 1 / self._clock_rate_mhz * 1000, units = 'ns').start())
        
    # Blocking write calls non blocking write function
    async def write(self, packet):
        self.write_nowait(packet)
    
    # Adds packet to the queue
    def write_nowait(self, packet):
        self.queue.append(packet)
        
    # Returns the number of packets
    def count(self):
        return len(self.queue)
    
    def empty(self):
        return not self.queue
    
    def clear(self):
        self.queue.clear()
        
    def _calculate_crc(self, data):
        crc = self._crc_init
        # TODO calculate crc
    
    async def _send_byte(self, byte, num_consecutive_ones):
        num_ones = num_consecutive_ones
        for i in range(8):
            # Grab the LSB
            bit = byte & 1
            byte >> 1
            
            # Send the bit
            await RisingEdge(self._clock)
            self._data.value = bit
            
            # If bit is 1 then we need to increase our counter
            if bit == 1:
                num_ones = num_ones + 1
            else:
                num_ones = 0
                
            # Determine if we need to zero fill
            if num_ones == 5:
                await RisingEdge(self._clock)
                self._data.value = 0
            
        return num_ones
            
    async def _run()
        while True:
            while not self.queue:
                # No data so send idle bytes
                await self._send_byte(0x7E, 0)
            
            # Grab the next packet
            packet = self.queue.popleft()
            
            # Calculate the CRC and append to the packet
            if self._append_crc:
                crc = self._calculate_crc(packet)
                packet.append(crc >> 8 & 0xFF)
                packet.append(crc & 0xFF)
            
            # Need to keep track of the number of consecutive ones
            num_consecutive_ones = 0
            for byte in packet:
                num_consecutive_ones = await self._send_byte(byte, num_consecutive_ones)
            
            # Send the idle byte to indicate the end of the packet
            await self._send_idle_byte(0x7E, 0)

class SyncSerialSink: