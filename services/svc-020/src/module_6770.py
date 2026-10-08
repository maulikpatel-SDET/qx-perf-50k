"""Service module 6770: business logic, no crypto."""


def calculate_total_6770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6770():
    return 'module 6770 handles orders and invoices'
