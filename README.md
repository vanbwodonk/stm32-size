# stm32-size
Python scripts for STM32 memory information

## Installation - Linux

```bash
git clone https://github.com/vanbwodonk/stm32-size.git
cd stm32-size
sudo python3 setup.py installl
```

## Usage

```bash
stm32-size [STM32-Chip-Family] [FILE.elf]
```
### Example

```bash
stm32-size STM32F103C8 firmware.elf 
```
output:
```bash
STM32-size memory usage firmware.elf
FLASH usage : [====     ]  43.2%  (used 28328 bytes from 65536 bytes)
RAM usage   : [=        ]  15.3%  (used 3124 bytes from 20480 bytes)
```
