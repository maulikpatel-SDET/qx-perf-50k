"""Service module 23522: business logic, no crypto."""


def calculate_total_23522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23522():
    return 'module 23522 handles orders and invoices'
