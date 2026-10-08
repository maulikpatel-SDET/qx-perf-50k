"""Service module 20972: business logic, no crypto."""


def calculate_total_20972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20972():
    return 'module 20972 handles orders and invoices'
