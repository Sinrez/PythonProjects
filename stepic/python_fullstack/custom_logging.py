import logging

extra_data = {'user' : 'ave@avecoders.com'}

def debug_log(): 
    logging.debug("Here's a debug-level log msg", extra=extra_data)

def main():

    dateStr = "%m/%d/%Y %I:%M:%S %p"

    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    
    logging.basicConfig(filename="output.log",
                        level= logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=dateStr)

    logging.info("Here's an info-level log message", extra=extra_data)
    logging.warning("Here's a warning-level log message", extra=extra_data)

    debug_log()
  



if __name__ == "__main__":
    main()