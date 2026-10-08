"""Service module 43963: business logic, no crypto."""


def calculate_total_43963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43963():
    return 'module 43963 handles orders and invoices'
