"""Service module 12481: business logic, no crypto."""


def calculate_total_12481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12481():
    return 'module 12481 handles orders and invoices'
