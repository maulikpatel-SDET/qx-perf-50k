"""Service module 20099: business logic, no crypto."""


def calculate_total_20099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20099():
    return 'module 20099 handles orders and invoices'
