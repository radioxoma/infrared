#!/usr/bin/env python

"""
Create LG remote config with all possible buttons.

Config can be inported in "Irplus" freeware.
    https://irplus-remote.github.io/
    https://play.google.com/store/apps/details?id=net.binarymode.android.irplus

irplus неверно обрабатывает нажатие кнопки: вместо отправки сигнала повторения он отправляет кнопку снова
"""

from xml.dom import minidom


stub = (
    ('manufacturer',   'LG'),
    ('model',          'reverse_config_0x0808'),
    ('columns',        '4'),

    ('format',         'WINLIRC_SPACEENC'),
    ('pre-bits',       '16'),
    ('bits',           '16'),
    ('toggle-bit-pos', '0'),
    ('gap-pulse',      '583'),
    ('gap-space',      '106945'),
    ('one-pulse',      '582'),
    ('one-space',      '1636'),
    ('zero-pulse',     '582'),
    ('zero-space',     '536'),
    ('header-pulse',   '4498'),
    ('header-space',   '4453'))


sequence = (
    ('KEY_CD',             '0xC03F'),
    ('KEY_AUX',            '0x906F'),
    ('CD_PLAYPAUSE',       '0x20DF'),
    ('CD_PREVIOUS',        '0x609F'),
    ('CD_STOP',            '0xA05F'),
    ('CD_NEXT',            '0xE01F'),
    ('KEY_TAPE',           '0x10EF'),
    ('DECK_PLAY_BACKWARD', '0x30CF'),
    ('DECK_PLAY',          '0xB04F'),
    ('DECK_STOP',          '0x708F'),

    ('SURROUND',           '0xF10E'),

    ('CD_REPEAT',          '0x728D'),
    ('CD_PROGRAM',         '0xB24D'),
    ('EQ_PATTERN',         '0x02FD'),
    ('KEY_0',              '0xD22D'),
    ('KEY_1',              '0x827D'),
    ('KEY_2',              '0x42BD'),
    ('KEY_3',              '0xC23D'),
    ('KEY_4',              '0x22DD'),
    ('KEY_5',              '0xA25D'),
    ('KEY_6',              '0x629D'),
    ('KEY_7',              '0xE21D'),
    ('KEY_8',              '0x12ED'),
    ('KEY_9',              '0x926D'),
    ('? KEY_DSKIP',        '0x52AD'),             # No idea what it does

    ('KEY_SLEEP',          '0x43BC'),
    ('? KEY_FUNCTION',     '0x33CC'),             # Cycle through CD/USB/Tuner/Aux modes
    ('? KEY_CLOCK',        '0x837C'),             # Set time

    ('? KEY_RDS',          '0x06F9'),             # Radio Data System

    ('KEY_POWER',          '0x7887'),
    ('KEY_MUTE',           '0xF807'),
    ('KEY_VOLUMEUP',       '0xE817'),
    ('KEY_VOLUMEDOWN',     '0x6897'),
    ('KEY_CHANNELDOWN',    '0x48B7'),
    ('KEY_CHANNELUP',      '0xC837'),
    ('DECK_REWIND',        '0x08F7'),
    ('DECK_FASTFORWARD',   '0x8877'),
    ('DECK_RECORD',        '0xA857'),
    ('XDSS',               '0xB847'),

    ('? KEY_MODE',         '0xF906'),             # Display mode: change spectrum in the display window

    ('? KEY_SHUFFLE',      '0x0AF5'),             # Random play
    ('KEY_TUNER',          '0x9A65'),
    ('? KEY_BRIGHTNESS_CYCLE', '0x08087A85'),     # Turn on/off LED on the front panel (Button Dimmer)

    ('OAO',                '0x5CA3'),
    
    ('? KEY_USB',          '0xDC23'),             # Play MP3 files from USB key
    ('? KEY_PTY_SEARCH',   '0x9C63'),             # Program TYpe Search
    ('? KEY_XTS_PRO',      '0xFD02'),             # eXcellent True Sound Pro

    ('KEY_INFO',           '0xEE11'),
    ('? KEY_PTY',          '0x8E71'),             # Program TYpe
)


def append_inverted(cmd):
    """Invert and concatenate.

    Returns 8 bytes.

    append_inverted('0xD2')
    >>> 0xD22D
    """
    # print("{0:b} 0x{0:x}".format(cmd))
    sequence = (cmd << 8) + (255 - cmd)
    # print("{0:b} 0x{0:x}".format(sequence))
    return sequence


# def build_str(command, address=0x08):
#     """Build 32-bit (4 byte, unsigned long) sequense.
#     """
#     data = "{:08b}{:08b}{:016b}".format(address, address, append_inverted(command))
#     print(data)
#     print("{:032b}".format(int(data, 2)))
#     print(int(data, 2))


def read_config():
    """Read part of an LG remote LIRC config and print it in reverse-engeneered form.

    Если заменить биты местами, то тогда последовательность кнопок 1, 2, 3 etc
    имеет смысл.

    KEY_1 65
    KEY_2 66
    KEY_3 67
    KEY_4 68
    KEY_5 69
    KEY_6 70
    KEY_7 71
    KEY_8 72
    KEY_9 73

    KEY_0 75

    ***

    NEC corporation protocol? Может быть format="WINLIRC_NEC1"?
    1 - большие паузы между горением светодиода
    0 - малые паузы между горением светодиода

    least significant bit first order?

    32 bit (4 byte) command:
        8 bit of address 0x08
        8 bit of address (repeat 0x08 with no modification)
        8 bit of command:
            4 bit - собственно команда, например клавиша 1 "0x1000"
            4 bit - вероятно указание на группу функций, например "Цифровые клавиши", "Старт-стоп"
        8 bit of logical inverce of command (в противофазе)

    Если swap четыре бита из cmd, то получится цифра.

    / addr 0x0808 \\/ cmd \\/ inv \\
    0000100000001000        ~~~~~~~~
    00001000000010001000001001111101 one   # 0b10000010, 0b01111101
    00001000000010000100001010111101 two   # 0b01000010, 0b10111101
    00001000000010001100001000111101 three # 0b00111101, 0b11000010
    00001000000010000010001011011101 four  # 0b00100010, 0b11011101 
    00001000000010000001001011101101 eight # 0b00010010, 0b11101101
    00001000000010001001001001101101 nine  # 0b10010010, 0b01001001
                    cmd  grp
                    0001 1 - реверс?
                    0010 2
                    0100 4
                    1000 8
    """
    def build_bytearray(command, address=0x08):
        """Build 32-bit (4 byte) sequense from LIRC file.

        :command: is 1 byte int
        """
        ba = bytearray(4)
        ba[:2] = address, address
        ba[2] = command
        ba[3] = 255 - command  # Inverted command
        print("/ addr \\/ addr \\/ cmd  \\/  inv \\ Btn 0x{:02x}   int".format(command))
        print("{:032b} 0x{} {}".format(
            int.from_bytes(ba, byteorder="big"), ba.hex(), int(ba.hex(), 16)))
        return ba

    assert 0b10010101 == 149  # LSB
    for btn, code in sequence:
        build_bytearray(int(code[:4], 16))  # Print bytes of each known command
    config = list()
    report = list()
    for btn, code in sequence:
        swap_bytes = "{:08b}".format(int(code[:4], 16))[::-1]
        cmd_first, cmd_last = swap_bytes[:4], swap_bytes[4:]
        group, command = int(cmd_first, 2), int(cmd_last, 2)
        report.append("Code {:3.0f}, group {} ({:2.0f}), command {} ({:2.0f}) - {}".format(
            int(swap_bytes, 2), cmd_first, group, cmd_last, command, btn))
        # config.append((code, group, command, btn))
    # config.sort(key=operator.itemgetter(1, 2))
    # pprint(config)
    report.sort()
    print('\n'.join(report))


def create_full_irplus_config():
    """Creates irplus XML config with all possible 256 keys.
    """
    lirc_codes = dict((int(c, 16), l) for l, c in sequence)

    config = minidom.Document()
    irplus = config.createElement('irplus')
    config.appendChild(irplus)

    device = config.createElement('device')
    for pair in stub:
        device.setAttribute(*pair)
    irplus.appendChild(device)

    for group in range(16):
        for command in range(16):
            first_half = int("{:04b}{:04b}".format(group, command)[::-1], 2)
            full_cmd = (first_half << 8) + (255 - first_half)
            # print(hex(full_cmd), group)
            # print("{}{}".format(command_swapb, group_swapb))

            button = config.createElement('button')
            button.setAttribute('span', '1')
            if full_cmd in lirc_codes:
                label_str = lirc_codes[full_cmd]
            else:
                label_str = "{:2.0f} {:2.0f}".format(group, command)
            button.setAttribute('label', label_str)
            button.appendChild(config.createTextNode('0x808 0x{:04x}'.format(full_cmd)))
            device.appendChild(button)

    xml_str = config.toprettyxml(indent="  ")
    with open("lg_6710CMA_0x0808_full_irplus_config.xml", "w") as f:
        f.write(xml_str)
    # print(xml_str)


if __name__ == '__main__':
    # read_config()
    create_full_irplus_config()
