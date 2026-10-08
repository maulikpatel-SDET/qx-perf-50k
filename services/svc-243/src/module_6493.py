"""Service module 6493: business logic, no crypto."""


def calculate_total_6493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6493():
    return 'module 6493 handles orders and invoices'
