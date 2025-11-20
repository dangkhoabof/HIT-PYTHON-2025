def create_item(name, qty, price):
    return {"name": name, "qty": qty, "price": price}


def calc_total(items):
    total = 0
    for item in items:
        total += item["qty"] * item["price"]
    return total



def format_invoice(customer, items):
    lines = []
    lines.append(f"Customer: {customer}")
    lines.append("-" * 40)
    lines.append(f"{'Product':<15} {'Qty':>6} {'Price':>12} {'Subtotal':>15}")

    total = 0
    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        subtotal = qty * price
        total += subtotal
        lines.append(f"{name:<15} {qty:>6} {price:>11.1f} {subtotal:>15.1f}")
    lines.append("-" * 40)
    lines.append(f"TOTAL: {total:.1f}")

    return "\n".join(lines)


def export_text(invoice_string):
    return invoice_string.split("\n")



items = [
    create_item("Pen", 2, 5.0),
    create_item("Notebook", 1, 15.0)
]

print(format_invoice("Nguyen Van A", items))
print("\n".join(export_text(format_invoice("Nguyen Van A", items))))