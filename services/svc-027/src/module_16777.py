"""Service module 16777: business logic, no crypto."""


def calculate_total_16777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16777():
    return 'module 16777 handles orders and invoices'
