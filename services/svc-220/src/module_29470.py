"""Service module 29470: business logic, no crypto."""


def calculate_total_29470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29470():
    return 'module 29470 handles orders and invoices'
