"""Service module 15370: business logic, no crypto."""


def calculate_total_15370(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15370():
    return 'module 15370 handles orders and invoices'
