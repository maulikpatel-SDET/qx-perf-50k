"""Service module 33602: business logic, no crypto."""


def calculate_total_33602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33602():
    return 'module 33602 handles orders and invoices'
