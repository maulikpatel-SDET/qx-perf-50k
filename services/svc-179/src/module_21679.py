"""Service module 21679: business logic, no crypto."""


def calculate_total_21679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21679():
    return 'module 21679 handles orders and invoices'
