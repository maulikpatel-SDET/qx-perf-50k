"""Service module 39431: business logic, no crypto."""


def calculate_total_39431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39431():
    return 'module 39431 handles orders and invoices'
