"""Service module 40351: business logic, no crypto."""


def calculate_total_40351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40351():
    return 'module 40351 handles orders and invoices'
