"""Service module 49522: business logic, no crypto."""


def calculate_total_49522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49522():
    return 'module 49522 handles orders and invoices'
