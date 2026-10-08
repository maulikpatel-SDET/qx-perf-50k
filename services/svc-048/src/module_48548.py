"""Service module 48548: business logic, no crypto."""


def calculate_total_48548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48548():
    return 'module 48548 handles orders and invoices'
