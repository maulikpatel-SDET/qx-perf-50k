"""Service module 37504: business logic, no crypto."""


def calculate_total_37504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37504():
    return 'module 37504 handles orders and invoices'
