"""Service module 25646: business logic, no crypto."""


def calculate_total_25646(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25646():
    return 'module 25646 handles orders and invoices'
