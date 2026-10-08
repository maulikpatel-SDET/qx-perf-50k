"""Service module 6099: business logic, no crypto."""


def calculate_total_6099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6099():
    return 'module 6099 handles orders and invoices'
