"""Service module 39661: business logic, no crypto."""


def calculate_total_39661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39661():
    return 'module 39661 handles orders and invoices'
