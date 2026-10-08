"""Service module 12504: business logic, no crypto."""


def calculate_total_12504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12504():
    return 'module 12504 handles orders and invoices'
