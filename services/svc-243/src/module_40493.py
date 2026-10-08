"""Service module 40493: business logic, no crypto."""


def calculate_total_40493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40493():
    return 'module 40493 handles orders and invoices'
