"""Service module 13972: business logic, no crypto."""


def calculate_total_13972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13972():
    return 'module 13972 handles orders and invoices'
