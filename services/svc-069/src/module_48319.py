"""Service module 48319: business logic, no crypto."""


def calculate_total_48319(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48319():
    return 'module 48319 handles orders and invoices'
