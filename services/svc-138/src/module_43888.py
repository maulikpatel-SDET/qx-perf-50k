"""Service module 43888: business logic, no crypto."""


def calculate_total_43888(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43888():
    return 'module 43888 handles orders and invoices'
