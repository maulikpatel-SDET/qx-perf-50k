"""Service module 39782: business logic, no crypto."""


def calculate_total_39782(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39782():
    return 'module 39782 handles orders and invoices'
