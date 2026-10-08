"""Service module 3602: business logic, no crypto."""


def calculate_total_3602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3602():
    return 'module 3602 handles orders and invoices'
