"""Service module 40262: business logic, no crypto."""


def calculate_total_40262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40262():
    return 'module 40262 handles orders and invoices'
