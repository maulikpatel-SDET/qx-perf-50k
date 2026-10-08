"""Service module 46262: business logic, no crypto."""


def calculate_total_46262(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46262():
    return 'module 46262 handles orders and invoices'
