"""Service module 26321: business logic, no crypto."""


def calculate_total_26321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26321():
    return 'module 26321 handles orders and invoices'
