"""Service module 28522: business logic, no crypto."""


def calculate_total_28522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28522():
    return 'module 28522 handles orders and invoices'
