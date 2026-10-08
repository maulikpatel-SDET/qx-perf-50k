"""Service module 4566: business logic, no crypto."""


def calculate_total_4566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4566():
    return 'module 4566 handles orders and invoices'
