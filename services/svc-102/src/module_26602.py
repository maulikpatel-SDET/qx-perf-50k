"""Service module 26602: business logic, no crypto."""


def calculate_total_26602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26602():
    return 'module 26602 handles orders and invoices'
