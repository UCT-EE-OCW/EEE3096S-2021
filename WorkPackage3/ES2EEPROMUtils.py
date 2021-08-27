"""
Code originally by CRImier
https://www.raspberrypi.org/forums/viewtopic.php?p=1401819#p1401819

Modified by Keegan Crankshaw for EEE3096S 2020
"""

from smbus2 import SMBus as SMBus2, i2c_msg
from math import ceil
from time import sleep


class ES2EEPROM:
    def __init__(self, bus=SMBus2(1), address=0x50):
        self.bus = bus
        self.address = address

    def write_block(self, start_block, data, bs=32, sleep_time=0.01):
        """
        Write data in blocks, starting at pos start_block.

        :param start_block: The starting block
        :param data: The data to write
        :param bs: The block size. Set at 32 for this EEPROM
        :param sleep_time: A default value to delay between operations

        """

        start_block = start_block*4
        b_l = len(data)
        # Last block may not be complete if data length not divisible by block size
        b_c = int(ceil(b_l/float(bs)))  # Block count
        # Actually splitting our data into blocks
        blocks = [data[bs*x:][:bs] for x in range(b_c)]
        for i, block in enumerate(blocks):
            if sleep_time:
                sleep(sleep_time)
            start = i*bs+start_block
            hb, lb = start >> 8, start & 0xff
            data = [hb, lb]+block
            write = i2c_msg.write(self.address, data)
            self.bus.i2c_rdwr(write)

    def write_byte(self, reg, data):
        """
        Write a single byte to a specified register

        :param reg: The register to write to
        :param data: The byte to write

        """

        hb, lb = reg >> 8, reg & 0xff
        data = [hb, lb, data]
        write = i2c_msg.write(self.address, data)
        self.bus.i2c_rdwr(write)
        sleep(0.01)

    def read_block(self, start_block, count, bs=32):
        """
        Reads multiple registers starting at a given block.

        :param start_block: The starting block
        :param count: THe amount of registers to read
        :param bs: Standard block size of 32 bits
        :return: None

        """

        start_block = start_block*4
        data = []  # We'll add our read results to here
        # If read count is not divisible by block size,
        # we'll have one partial read at the last read
        full_reads, remainder = divmod(count, bs)
        if remainder:
            full_reads += 1  # adding that last read if needed
        for i in range(full_reads):
            start = i*bs+start_block  # next block address
            hb, lb = start >> 8, start & 0xff  # into high and low byte
            write = i2c_msg.write(self.address, [hb, lb])
            # If we're on last cycle and remainder != 0, not doing a full read
            count = remainder if (remainder and i == full_reads-1) else bs
            read = i2c_msg.read(self.address, count)
            self.bus.i2c_rdwr(write, read)  # combined read&write
            data += list(read)
        return data

    def read_byte(self, reg):
        """
        Read a singly byte from a defined register.

        :param reg: The register to read from.
        :return: A single byte.

        """
        hb, lb = reg >> 8, reg & 0xff  # into high and low byte
        write = i2c_msg.write(self.address, [hb, lb])
        read = i2c_msg.read(self.address, 1)
        self.bus.i2c_rdwr(write, read)  # combined read&write
        return list(read)[0]

    def clear(self, length):
        """
        Clears a given amount of registers starting at position 0
        Useful for clearing the EEPROM

        :param length: The amount of registers to clear.
        :return:
        """
        self.write_block(0, [0x00]*length)

    def populate_mock_scores(self):
        """
        Populates three mock scores in EEPROM
        :return:
        """

        # First 4 bytes contain how many scores there are
        self.write_block(0, [4])
        scores = [["ChB", 5], ["Ada", 7], ["LSu", 4], ["EEE", 8]]
        scores.sort(key=lambda x: x[1])
        data_to_write = []
        for score in scores:
            # get the string
            for letter in score[0]:
                data_to_write.append(ord(letter))
            data_to_write.append(score[1])
        self.write_block(1, data_to_write)


if __name__ == "__main__":
    eeprom = ES2EEPROM()
    eeprom.clear(4096)
    eeprom.populate_mock_scores()

