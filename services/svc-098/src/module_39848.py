"""Service module 39848: business logic, no crypto."""


def calculate_total_39848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39848():
    return 'module 39848 handles orders and invoices'
