"""Service module 20374: business logic, no crypto."""


def calculate_total_20374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20374():
    return 'module 20374 handles orders and invoices'
