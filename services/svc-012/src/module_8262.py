"""Service module 8262: business logic, no crypto."""


def calculate_total_8262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8262():
    return 'module 8262 handles orders and invoices'
