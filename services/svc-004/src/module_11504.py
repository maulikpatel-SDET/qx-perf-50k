"""Service module 11504: business logic, no crypto."""


def calculate_total_11504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11504():
    return 'module 11504 handles orders and invoices'
