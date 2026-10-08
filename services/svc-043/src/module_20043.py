"""Service module 20043: business logic, no crypto."""


def calculate_total_20043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20043():
    return 'module 20043 handles orders and invoices'
