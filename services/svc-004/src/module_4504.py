"""Service module 4504: business logic, no crypto."""


def calculate_total_4504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4504():
    return 'module 4504 handles orders and invoices'
