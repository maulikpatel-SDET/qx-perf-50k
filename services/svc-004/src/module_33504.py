"""Service module 33504: business logic, no crypto."""


def calculate_total_33504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33504():
    return 'module 33504 handles orders and invoices'
