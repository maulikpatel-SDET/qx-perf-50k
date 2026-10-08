"""Service module 33911: business logic, no crypto."""


def calculate_total_33911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33911():
    return 'module 33911 handles orders and invoices'
