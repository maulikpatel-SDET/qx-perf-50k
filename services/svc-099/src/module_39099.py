"""Service module 39099: business logic, no crypto."""


def calculate_total_39099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39099():
    return 'module 39099 handles orders and invoices'
