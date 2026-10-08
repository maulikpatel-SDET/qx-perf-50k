"""Service module 12162: business logic, no crypto."""


def calculate_total_12162(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12162():
    return 'module 12162 handles orders and invoices'
