"""Service module 12777: business logic, no crypto."""


def calculate_total_12777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12777():
    return 'module 12777 handles orders and invoices'
