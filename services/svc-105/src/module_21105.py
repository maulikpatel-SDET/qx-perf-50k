"""Service module 21105: business logic, no crypto."""


def calculate_total_21105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21105():
    return 'module 21105 handles orders and invoices'
