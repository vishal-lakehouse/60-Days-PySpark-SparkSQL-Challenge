"""
===========================================================
60 Days PySpark & Spark SQL Challenge
Dataset Generator

Author : Vishal Kumar
Company: LakeMart Retail Corporation
===========================================================
"""

from config import *

import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker("en_IN")

print("=" * 60)
print("LakeMart Retail Dataset Generator")
print("=" * 60)

print(f"Customers   : {CUSTOMERS}")
print(f"Products    : {PRODUCTS}")
print(f"Stores      : {STORES}")
print(f"Orders      : {ORDERS}")
print(f"Order Items : {ORDER_ITEMS}")
print(f"Payments    : {PAYMENTS}")
print(f"Inventory   : {INVENTORY}")

print("\nDataset generation will start here...")
