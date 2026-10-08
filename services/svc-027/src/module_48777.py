"""Service module 48777: business logic, no crypto."""


def calculate_total_48777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48777():
    return 'module 48777 handles orders and invoices'
