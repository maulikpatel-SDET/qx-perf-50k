"""Service module 39784: business logic, no crypto."""


def calculate_total_39784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39784():
    return 'module 39784 handles orders and invoices'
