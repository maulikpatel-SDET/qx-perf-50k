"""Service module 18834: business logic, no crypto."""


def calculate_total_18834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18834():
    return 'module 18834 handles orders and invoices'
