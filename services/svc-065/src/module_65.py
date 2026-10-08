"""Service module 65: business logic, no crypto."""


def calculate_total_65(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_65():
    return 'module 65 handles orders and invoices'
