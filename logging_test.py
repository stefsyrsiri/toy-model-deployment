from loguru import logger

def divide(a, b):
    return a / b

logger.info("calculating a / b")
print(divide(2, 3))