"""Service module 27081: business logic, no crypto."""


def calculate_total_27081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27081():
    return 'module 27081 handles orders and invoices'
