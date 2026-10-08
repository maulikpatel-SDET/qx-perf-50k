"""Service module 2972: business logic, no crypto."""


def calculate_total_2972(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2972():
    return 'module 2972 handles orders and invoices'
