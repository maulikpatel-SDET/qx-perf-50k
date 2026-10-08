"""Service module 2782: business logic, no crypto."""


def calculate_total_2782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2782():
    return 'module 2782 handles orders and invoices'
