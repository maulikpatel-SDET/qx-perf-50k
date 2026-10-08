"""Service module 38679: business logic, no crypto."""


def calculate_total_38679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38679():
    return 'module 38679 handles orders and invoices'
