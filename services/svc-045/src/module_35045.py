"""Service module 35045: business logic, no crypto."""


def calculate_total_35045(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35045():
    return 'module 35045 handles orders and invoices'
