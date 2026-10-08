"""Service module 14504: business logic, no crypto."""


def calculate_total_14504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14504():
    return 'module 14504 handles orders and invoices'
