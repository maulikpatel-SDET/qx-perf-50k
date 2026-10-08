"""Service module 11276: business logic, no crypto."""


def calculate_total_11276(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11276():
    return 'module 11276 handles orders and invoices'
