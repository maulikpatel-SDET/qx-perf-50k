"""Service module 1782: business logic, no crypto."""


def calculate_total_1782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1782():
    return 'module 1782 handles orders and invoices'
