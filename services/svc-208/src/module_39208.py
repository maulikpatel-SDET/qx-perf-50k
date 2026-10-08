"""Service module 39208: business logic, no crypto."""


def calculate_total_39208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39208():
    return 'module 39208 handles orders and invoices'
