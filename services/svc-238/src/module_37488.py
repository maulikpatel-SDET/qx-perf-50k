"""Service module 37488: business logic, no crypto."""


def calculate_total_37488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37488():
    return 'module 37488 handles orders and invoices'
