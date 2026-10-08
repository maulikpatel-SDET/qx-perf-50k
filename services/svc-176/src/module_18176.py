"""Service module 18176: business logic, no crypto."""


def calculate_total_18176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18176():
    return 'module 18176 handles orders and invoices'
