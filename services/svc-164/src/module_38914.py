"""Service module 38914: business logic, no crypto."""


def calculate_total_38914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38914():
    return 'module 38914 handles orders and invoices'
