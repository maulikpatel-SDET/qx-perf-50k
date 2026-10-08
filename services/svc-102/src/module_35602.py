"""Service module 35602: business logic, no crypto."""


def calculate_total_35602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35602():
    return 'module 35602 handles orders and invoices'
