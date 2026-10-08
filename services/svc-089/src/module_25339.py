"""Service module 25339: business logic, no crypto."""


def calculate_total_25339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25339():
    return 'module 25339 handles orders and invoices'
