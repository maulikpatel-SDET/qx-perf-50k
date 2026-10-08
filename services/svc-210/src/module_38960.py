"""Service module 38960: business logic, no crypto."""


def calculate_total_38960(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38960():
    return 'module 38960 handles orders and invoices'
