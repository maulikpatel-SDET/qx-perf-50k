"""Service module 34504: business logic, no crypto."""


def calculate_total_34504(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34504():
    return 'module 34504 handles orders and invoices'
