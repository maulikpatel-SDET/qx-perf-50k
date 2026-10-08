"""Service module 35843: business logic, no crypto."""


def calculate_total_35843(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35843():
    return 'module 35843 handles orders and invoices'
