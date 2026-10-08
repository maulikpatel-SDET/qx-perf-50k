"""Service module 46007: business logic, no crypto."""


def calculate_total_46007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46007():
    return 'module 46007 handles orders and invoices'
