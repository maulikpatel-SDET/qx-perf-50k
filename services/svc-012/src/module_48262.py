"""Service module 48262: business logic, no crypto."""


def calculate_total_48262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48262():
    return 'module 48262 handles orders and invoices'
