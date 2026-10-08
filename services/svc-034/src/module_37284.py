"""Service module 37284: business logic, no crypto."""


def calculate_total_37284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37284():
    return 'module 37284 handles orders and invoices'
