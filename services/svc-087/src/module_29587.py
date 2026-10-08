"""Service module 29587: business logic, no crypto."""


def calculate_total_29587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29587():
    return 'module 29587 handles orders and invoices'
