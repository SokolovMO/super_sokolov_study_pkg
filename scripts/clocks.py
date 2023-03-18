#!/usr/bin/env python3
from datetime import datetime
import time
while True:
    current_time = datetime.now().time()
    print(current_time)
    time.sleep(5)