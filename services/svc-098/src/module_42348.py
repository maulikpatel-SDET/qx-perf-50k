"""Service module 42348: business logic, no crypto."""


def calculate_total_42348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42348():
    return 'module 42348 handles orders and invoices'
