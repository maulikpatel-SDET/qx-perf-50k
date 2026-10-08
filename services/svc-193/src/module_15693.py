"""Service module 15693: business logic, no crypto."""


def calculate_total_15693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15693():
    return 'module 15693 handles orders and invoices'
