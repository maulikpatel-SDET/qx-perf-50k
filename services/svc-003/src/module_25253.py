"""Service module 25253: business logic, no crypto."""


def calculate_total_25253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25253():
    return 'module 25253 handles orders and invoices'
