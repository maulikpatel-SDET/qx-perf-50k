"""Service module 30602: business logic, no crypto."""


def calculate_total_30602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30602():
    return 'module 30602 handles orders and invoices'
