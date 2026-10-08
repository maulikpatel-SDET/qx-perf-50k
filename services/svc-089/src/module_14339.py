"""Service module 14339: business logic, no crypto."""


def calculate_total_14339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14339():
    return 'module 14339 handles orders and invoices'
