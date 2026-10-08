"""Service module 2208: business logic, no crypto."""


def calculate_total_2208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2208():
    return 'module 2208 handles orders and invoices'
