import logging

# 需求：a==1的时候，flag = True
a = 1
b = 2
if a == 1:
    flag = False
    logging.info(f"a==1:flag={flag}")
else:
    flag = True
