"""Service module 41990: business logic, no crypto."""


def calculate_total_41990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41990():
    return 'module 41990 handles orders and invoices'
