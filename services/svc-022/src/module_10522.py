"""Service module 10522: business logic, no crypto."""


def calculate_total_10522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10522():
    return 'module 10522 handles orders and invoices'
