"""Service module 43150: business logic, no crypto."""


def calculate_total_43150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43150():
    return 'module 43150 handles orders and invoices'
