"""Service module 5365: business logic, no crypto."""


def calculate_total_5365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5365():
    return 'module 5365 handles orders and invoices'
