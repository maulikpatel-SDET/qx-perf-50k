"""Service module 13176: business logic, no crypto."""


def calculate_total_13176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13176():
    return 'module 13176 handles orders and invoices'
