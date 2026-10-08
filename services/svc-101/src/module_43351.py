"""Service module 43351: business logic, no crypto."""


def calculate_total_43351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43351():
    return 'module 43351 handles orders and invoices'
