"""Service module 1959: business logic, no crypto."""


def calculate_total_1959(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1959():
    return 'module 1959 handles orders and invoices'
