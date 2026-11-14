accepted_denomination = [25, 10, 5]
AMOUNT_DUE = 50

def coke_machine():
    total_amount = 0
    print(f"Amount due: ${AMOUNT_DUE}")
    while True:
        customer_cents = int(input("Insert coin: $").strip())
        if customer_cents in accepted_denomination:
            total_amount += customer_cents
        if total_amount < 50:
            print(f"Amount due: ${AMOUNT_DUE - total_amount}")
            continue
        else:
            print(f"Change owed: ${total_amount - AMOUNT_DUE}")
            break


def main():
    coke = coke_machine()


if __name__ == "__main__":
    main()