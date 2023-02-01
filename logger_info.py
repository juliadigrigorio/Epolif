import logging

logging.basicConfig(
    level="INFO",
    filename="Mylog.log",
    filemode="w",
    format="%(asctime)s::%(levelname)s::%(message)s",
)

logger = logging.getLogger()
# print(logger.level)
handlers = logger.handlers


def main(name):
    logger.warning(f"Enter in the main function: name= {name}")
    logger.info(f"Enter in the main function: name= {name}")
    logger.debug(f"Enter in the main function: name= {name}")


if __name__ == "__main__":
    main("Example")
