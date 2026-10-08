"""Service module 3099: business logic, no crypto."""


def calculate_total_3099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3099():
    return 'module 3099 handles orders and invoices'
