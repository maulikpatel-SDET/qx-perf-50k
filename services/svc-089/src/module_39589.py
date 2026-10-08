"""Service module 39589: business logic, no crypto."""


def calculate_total_39589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39589():
    return 'module 39589 handles orders and invoices'
