"""Service module 14522: business logic, no crypto."""


def calculate_total_14522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14522():
    return 'module 14522 handles orders and invoices'
