"""Service module 20247: business logic, no crypto."""


def calculate_total_20247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20247():
    return 'module 20247 handles orders and invoices'
