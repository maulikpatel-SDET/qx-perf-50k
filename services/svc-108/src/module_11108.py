"""Service module 11108: business logic, no crypto."""


def calculate_total_11108(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11108():
    return 'module 11108 handles orders and invoices'
