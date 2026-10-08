"""Service module 15319: business logic, no crypto."""


def calculate_total_15319(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15319():
    return 'module 15319 handles orders and invoices'
