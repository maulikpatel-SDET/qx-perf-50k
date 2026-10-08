"""Service module 47602: business logic, no crypto."""


def calculate_total_47602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47602():
    return 'module 47602 handles orders and invoices'
