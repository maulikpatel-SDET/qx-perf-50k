"""Service module 44176: business logic, no crypto."""


def calculate_total_44176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44176():
    return 'module 44176 handles orders and invoices'
