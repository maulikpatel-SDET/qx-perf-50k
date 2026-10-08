"""Service module 16108: business logic, no crypto."""


def calculate_total_16108(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16108():
    return 'module 16108 handles orders and invoices'
