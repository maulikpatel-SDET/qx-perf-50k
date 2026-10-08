"""Service module 21208: business logic, no crypto."""


def calculate_total_21208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21208():
    return 'module 21208 handles orders and invoices'
