import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Инициализация I2C и ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Читаем с A0

while True:
    voltage = chan.voltage  # Получаем напряжение (0-3.3V)
    resistance = (3.3 - voltage) / voltage * 10000  # Формула для расчета сопротивления
    print(f"Voltage: {voltage:.3f}V | Resistance: {resistance:.2f}Ω")
    time.sleep(0.1)
