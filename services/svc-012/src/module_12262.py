"""Service module 12262: business logic, no crypto."""


def calculate_total_12262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12262():
    return 'module 12262 handles orders and invoices'
