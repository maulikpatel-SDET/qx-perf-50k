"""Service module 40218: business logic, no crypto."""


def calculate_total_40218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40218():
    return 'module 40218 handles orders and invoices'
