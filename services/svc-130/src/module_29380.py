"""Service module 29380: business logic, no crypto."""


def calculate_total_29380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29380():
    return 'module 29380 handles orders and invoices'
