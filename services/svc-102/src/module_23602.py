"""Service module 23602: business logic, no crypto."""


def calculate_total_23602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23602():
    return 'module 23602 handles orders and invoices'
