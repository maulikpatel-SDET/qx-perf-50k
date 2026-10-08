"""Service module 1339: business logic, no crypto."""


def calculate_total_1339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1339():
    return 'module 1339 handles orders and invoices'
