"""Service module 43176: business logic, no crypto."""


def calculate_total_43176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43176():
    return 'module 43176 handles orders and invoices'
