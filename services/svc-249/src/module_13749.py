"""Service module 13749: business logic, no crypto."""


def calculate_total_13749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13749():
    return 'module 13749 handles orders and invoices'
