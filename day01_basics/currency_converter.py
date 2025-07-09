def convert(amount, rate):
    return round(amount * rate, 2)

eur = float(input("Zadaj sumu v EUR: "))
rate = 1.1  # napr. kurz pre USD
usd = convert(eur, rate)
print(f"{eur} EUR je približne {usd} USD")

def convert(amount, rate):
    return round(amount * rate, 2)


# Používateľ zadá sumu v EUR
try:
    eur = float(input("Zadaj sumu v EUR: "))
    print("\nPrepočty:")

    usd_rate = 1.08
    czk_rate = 24.7
    huf_rate = 435.0

    print(f"{eur} EUR = {convert(eur, usd_rate)} USD")
    print(f"{eur} EUR = {convert(eur, czk_rate)} CZK")
    print(f"{eur} EUR = {convert(eur, huf_rate)} HUF")

except ValueError:
    print("Neplatná hodnota – zadaj číslo s bodkou (napr. 42.5)")