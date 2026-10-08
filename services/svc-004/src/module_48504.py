"""Service module 48504: business logic, no crypto."""


def calculate_total_48504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48504():
    return 'module 48504 handles orders and invoices'
