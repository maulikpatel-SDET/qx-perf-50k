"""Service module 33749: business logic, no crypto."""


def calculate_total_33749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33749():
    return 'module 33749 handles orders and invoices'
