"""Service module 38141: business logic, no crypto."""


def calculate_total_38141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38141():
    return 'module 38141 handles orders and invoices'
