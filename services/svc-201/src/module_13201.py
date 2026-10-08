"""Service module 13201: business logic, no crypto."""


def calculate_total_13201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13201():
    return 'module 13201 handles orders and invoices'
