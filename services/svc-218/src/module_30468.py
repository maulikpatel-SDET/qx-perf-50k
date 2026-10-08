"""Service module 30468: business logic, no crypto."""


def calculate_total_30468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30468():
    return 'module 30468 handles orders and invoices'
