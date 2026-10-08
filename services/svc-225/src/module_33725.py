"""Service module 33725: business logic, no crypto."""


def calculate_total_33725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33725():
    return 'module 33725 handles orders and invoices'
