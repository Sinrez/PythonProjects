import logging

def main():

    logging.basicConfig(level=logging.DEBUG,
                        filename="log_output.log",
                        filemode="w")


    logging.debug("Here's a debug-level log message")
    logging.info("Here's an info-level log message")
    logging.warning("Here's a warning-level message")
    logging.error("Here's an error-level message")
    logging.critical("Here's a critical-level message")

    logging.warning("Here's a {} variable and an int:".format("string", 42))

if __name__ == "__main__":
    main()
