"""Service module 33851: business logic, no crypto."""


def calculate_total_33851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33851():
    return 'module 33851 handles orders and invoices'
