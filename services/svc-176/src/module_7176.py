"""Service module 7176: business logic, no crypto."""


def calculate_total_7176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7176():
    return 'module 7176 handles orders and invoices'
