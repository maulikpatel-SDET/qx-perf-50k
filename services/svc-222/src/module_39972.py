"""Service module 39972: business logic, no crypto."""


def calculate_total_39972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39972():
    return 'module 39972 handles orders and invoices'
