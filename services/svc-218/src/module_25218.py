"""Service module 25218: business logic, no crypto."""


def calculate_total_25218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25218():
    return 'module 25218 handles orders and invoices'
