"""Service module 37468: business logic, no crypto."""


def calculate_total_37468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37468():
    return 'module 37468 handles orders and invoices'
