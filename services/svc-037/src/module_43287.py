"""Service module 43287: business logic, no crypto."""


def calculate_total_43287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43287():
    return 'module 43287 handles orders and invoices'
