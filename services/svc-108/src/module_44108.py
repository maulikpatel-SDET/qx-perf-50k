"""Service module 44108: business logic, no crypto."""


def calculate_total_44108(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44108():
    return 'module 44108 handles orders and invoices'
