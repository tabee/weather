import logging
import weather

# add a logger
logger = logging.getLogger('weather_logger')
hdlr = logging.FileHandler('example.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)



#message = weather.Weather('rubigen', 'ch') # data from parameter
message = weather.Weather(city=False,country=False)  # data from config.json
logger.info(message)