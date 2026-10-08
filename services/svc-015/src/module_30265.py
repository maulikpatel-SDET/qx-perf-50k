"""Service module 30265: business logic, no crypto."""


def calculate_total_30265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30265():
    return 'module 30265 handles orders and invoices'
