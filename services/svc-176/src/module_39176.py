"""Service module 39176: business logic, no crypto."""


def calculate_total_39176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39176():
    return 'module 39176 handles orders and invoices'
