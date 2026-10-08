"""Service module 43279: business logic, no crypto."""


def calculate_total_43279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43279():
    return 'module 43279 handles orders and invoices'
