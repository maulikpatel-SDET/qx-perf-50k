"""Service module 11846: business logic, no crypto."""


def calculate_total_11846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11846():
    return 'module 11846 handles orders and invoices'
