"""Service module 17990: business logic, no crypto."""


def calculate_total_17990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17990():
    return 'module 17990 handles orders and invoices'
