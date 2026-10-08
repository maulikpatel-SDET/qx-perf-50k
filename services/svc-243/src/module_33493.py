"""Service module 33493: business logic, no crypto."""


def calculate_total_33493(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33493():
    return 'module 33493 handles orders and invoices'
