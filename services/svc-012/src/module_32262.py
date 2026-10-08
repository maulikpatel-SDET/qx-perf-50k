"""Service module 32262: business logic, no crypto."""


def calculate_total_32262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32262():
    return 'module 32262 handles orders and invoices'
