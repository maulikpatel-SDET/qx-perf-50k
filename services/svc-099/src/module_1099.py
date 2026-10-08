"""Service module 1099: business logic, no crypto."""


def calculate_total_1099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1099():
    return 'module 1099 handles orders and invoices'
