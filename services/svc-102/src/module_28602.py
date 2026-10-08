"""Service module 28602: business logic, no crypto."""


def calculate_total_28602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28602():
    return 'module 28602 handles orders and invoices'
