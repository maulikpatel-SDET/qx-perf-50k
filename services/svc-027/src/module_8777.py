"""Service module 8777: business logic, no crypto."""


def calculate_total_8777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8777():
    return 'module 8777 handles orders and invoices'
