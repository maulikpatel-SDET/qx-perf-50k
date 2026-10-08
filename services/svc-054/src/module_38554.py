"""Service module 38554: business logic, no crypto."""


def calculate_total_38554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38554():
    return 'module 38554 handles orders and invoices'
