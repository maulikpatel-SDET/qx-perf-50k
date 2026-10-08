"""Service module 30524: business logic, no crypto."""


def calculate_total_30524(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30524():
    return 'module 30524 handles orders and invoices'
