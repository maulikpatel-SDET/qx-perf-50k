"""Service module 5522: business logic, no crypto."""


def calculate_total_5522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5522():
    return 'module 5522 handles orders and invoices'
