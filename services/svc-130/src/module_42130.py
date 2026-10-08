"""Service module 42130: business logic, no crypto."""


def calculate_total_42130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42130():
    return 'module 42130 handles orders and invoices'
