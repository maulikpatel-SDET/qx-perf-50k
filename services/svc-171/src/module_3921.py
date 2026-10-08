"""Service module 3921: business logic, no crypto."""


def calculate_total_3921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3921():
    return 'module 3921 handles orders and invoices'
