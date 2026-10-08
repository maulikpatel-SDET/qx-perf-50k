"""Service module 2602: business logic, no crypto."""


def calculate_total_2602(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2602():
    return 'module 2602 handles orders and invoices'
