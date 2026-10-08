"""Service module 37914: business logic, no crypto."""


def calculate_total_37914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37914():
    return 'module 37914 handles orders and invoices'
