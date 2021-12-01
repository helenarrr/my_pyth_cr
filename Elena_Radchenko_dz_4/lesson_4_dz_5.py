import sys
from utilis_module import currency_rates_sp

if __name__ == "__main__":
    for i in sys.argv[1:]:
        currency_rates_sp(i)
    exit()