import datetime

# Mobiles list - model: price
mobiles = {
    "Samsung Galaxy A15": 45000,
    "Samsung Galaxy A35": 75000,
    "Samsung Galaxy S24": 180000,
    "iPhone 13": 180000,
    "iPhone 14": 220000,
    "iPhone 15": 280000,
    "Vivo Y18": 35000,
    "Vivo V29": 85000,
    "Oppo A58": 45000,
    "Oppo Reno 11": 95000,
    "Xiaomi Redmi 13C": 30000,
    "Xiaomi Note 13": 65000,
    "Tecno Spark 20": 28000,
    "Infinix Hot 40": 32000,
    "Nokia G21": 25000,
}

# Accessories list
accessories = {
    "Charger (Original)": 1500,
    "Charger (Copy)": 500,
    "Cover / Case": 300,
    "Tempered Glass": 200,
    "Earphones": 800,
    "Data Cable": 400,
    "Power Bank 10000mAh": 2500,
    "Memory Card 128GB": 2000,
    "Mobile Holder": 350,
    "Wireless Earbuds": 3500,
}

STORE_NAME = "THE CONNECTING HUB MOBILE SHOP"
STORE_ADDRESS = "KOTA RAJASTHAN"
STORE_PHONE = "7357503117"


def show_mobiles():
    print("\n--- Mobiles ---")
    print(f"  {'No':<4} {'Model':<30} {'Price'}")
    print("  " + "-" * 45)

    for i, (name, price) in enumerate(mobiles.items(), 1):
        print(f"  {i:<4} {name:<30} Rs. {price:,}")

    print("  " + "-" * 45)


def show_accessories():
    print("\n--- Accessories ---")
    print(f"  {'No':<4} {'Item':<25} {'Price'}")
    print("  " + "-" * 38)

    for i, (name, price) in enumerate(accessories.items(), 1):
        print(f"  {i:<4} {name:<25} Rs. {price:,}")

    print("  " + "-" * 38)


def make_bill():
    now = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
    bill_no = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    print(f"\n{'='*48}")
    print(f"       {STORE_NAME}")
    print(f"       {STORE_ADDRESS}")
    print(f"       Tel: {STORE_PHONE}")
    print(f"{'='*48}")

    customer = input("Customer Name (Enter to Skip): ").strip()

    phone = input("Phone Number (Enter to Skip): ").strip()

    if phone:
        while not (phone.isdigit() and len(phone) == 10):
            print("❌ Enter a valid 10-digit phone number")
            phone = input("Phone Number: ").strip()

    imei = input("IMEI Number (Enter to Skip): ").strip()

    if imei:
        while not (imei.isdigit() and len(imei) == 15):
            print("❌ Enter a valid 15-digit IMEI Number")
            imei = input("IMEI Number: ").strip()

    bill = []

    while True:
        print("\n--- What to Add? ---")
        print("1. Mobile")
        print("2. Accessory")
        print("0. Complete Bill")

        choice = input("Choose: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            show_mobiles()

            num = input("Select Mobile Number: ").strip()

            if not num.isdigit() or int(num) < 1 or int(num) > len(mobiles):
                print("❌ Invalid selection!")
                continue

            name, price = list(mobiles.items())[int(num) - 1]

            qty_input = input("Quantity: ").strip()

            if not qty_input.isdigit() or int(qty_input) < 1:
                print("❌ Invalid quantity!")
                continue

            qty = int(qty_input)
            total = qty * price

            bill.append(("📱 " + name, qty, price, total))
            print(f"✅ Added: {name} x{qty} = Rs. {total:,}")

        elif choice == "2":
            show_accessories()

            num = input("Select Accessory Number: ").strip()

            if not num.isdigit() or int(num) < 1 or int(num) > len(accessories):
                print("❌ Invalid selection!")
                continue

            name, price = list(accessories.items())[int(num) - 1]

            qty_input = input("Quantity: ").strip()

            if not qty_input.isdigit() or int(qty_input) < 1:
                print("❌ Invalid quantity!")
                continue

            qty = int(qty_input)
            total = qty * price

            bill.append(("🔌 " + name, qty, price, total))
            print(f"✅ Added: {name} x{qty} = Rs. {total:,}")

        else:
            print("❌ Please enter 0, 1 or 2")

    if not bill:
        print("\nBill is empty!")
        return

    disc_input = input("\nDiscount (Rs) [0 for none]: ").strip()
    discount = int(disc_input) if disc_input.isdigit() else 0

    subtotal = sum(t for _, _, _, t in bill)
    grand_total = subtotal - discount

    print(f"\n{'='*48}")
    print(f"        {STORE_NAME}")
    print(f"        {STORE_ADDRESS}")
    print(f"        Tel: {STORE_PHONE}")
    print(f"{'='*48}")

    print(f"Bill No : {bill_no}")
    print(f"Date    : {now}")

    if customer:
        print(f"Customer: {customer}")

    if phone:
        print(f"Phone   : {phone}")

    if imei:
        print(f"IMEI    : {imei}")

    print(f"{'-'*48}")
    print(f"{'Item':<28} {'Qty':>3} {'Price':>8} {'Total':>8}")
    print(f"{'-'*48}")

    for name, qty, price, total in bill:
        print(f"{name:<28} {qty:>3} {price:>8,} {total:>8,}")

    print(f"{'-'*48}")
    print(f"{'Subtotal':>40}: Rs. {subtotal:,}")

    if discount:
        print(f"{'Discount':>40}: Rs. {discount:,}")

    print(f"{'TOTAL':>40}: Rs. {grand_total:,}")
    print(f"{'='*48}")
    print("Thank You For Shopping With Us!")
    print(f"{'='*48}\n")

    save = input("Save Bill? (y/n): ").strip().lower()

    if save == "y":
        fname = f"mobile_bill_{bill_no}.txt"

        with open(fname, "w", encoding="utf-8") as f:
            f.write(f"{STORE_NAME}\n")
            f.write(f"{STORE_ADDRESS}\n")
            f.write(f"Tel: {STORE_PHONE}\n")
            f.write(f"Bill No: {bill_no}\n")
            f.write(f"Date: {now}\n")

            if customer:
                f.write(f"Customer: {customer}\n")

            if phone:
                f.write(f"Phone: {phone}\n")

            if imei:
                f.write(f"IMEI: {imei}\n")

            f.write("-" * 48 + "\n")

            for name, qty, price, total in bill:
                f.write(f"{name:<28} x{qty}  Rs.{total:,}\n")

            f.write("-" * 48 + "\n")
            f.write(f"Subtotal : Rs. {subtotal:,}\n")

            if discount:
                f.write(f"Discount : Rs. {discount:,}\n")

            f.write(f"TOTAL    : Rs. {grand_total:,}\n")

        print(f"✅ Bill Saved Successfully: {fname}")


def view_stock():
    print(f"\n{'='*48}")
    print("MOBILE STOCK")
    show_mobiles()

    print("\nACCESSORIES STOCK")
    show_accessories()


while True:
    print("\n" + "=" * 38)
    print(f"     {STORE_NAME}")
    print("=" * 38)
    print("1. Create Bill")
    print("2. Show Stock")
    print("3. Exit")
    print("=" * 38)

    choice = input("Choose (1/2/3): ").strip()

    if choice == "1":
        make_bill()

    elif choice == "2":
        view_stock()

    elif choice == "3":
        print("\nRadhe Radhe 🙏\n")
        break

    else:
        print("❌ Please enter 1, 2 or 3")
