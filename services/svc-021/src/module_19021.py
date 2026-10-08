"""Service module 19021: business logic, no crypto."""


def calculate_total_19021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19021():
    return 'module 19021 handles orders and invoices'
