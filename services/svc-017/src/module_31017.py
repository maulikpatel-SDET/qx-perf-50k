"""Service module 31017: business logic, no crypto."""


def calculate_total_31017(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31017():
    return 'module 31017 handles orders and invoices'
