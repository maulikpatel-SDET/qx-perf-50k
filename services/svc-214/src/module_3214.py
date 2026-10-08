"""Service module 3214: business logic, no crypto."""


def calculate_total_3214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3214():
    return 'module 3214 handles orders and invoices'
