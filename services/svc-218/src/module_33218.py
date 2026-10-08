"""Service module 33218: business logic, no crypto."""


def calculate_total_33218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33218():
    return 'module 33218 handles orders and invoices'
