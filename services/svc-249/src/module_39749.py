"""Service module 39749: business logic, no crypto."""


def calculate_total_39749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39749():
    return 'module 39749 handles orders and invoices'
