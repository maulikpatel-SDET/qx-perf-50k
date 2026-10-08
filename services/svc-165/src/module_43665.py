"""Service module 43665: business logic, no crypto."""


def calculate_total_43665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43665():
    return 'module 43665 handles orders and invoices'
