"""Service module 43290: business logic, no crypto."""


def calculate_total_43290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43290():
    return 'module 43290 handles orders and invoices'
