"""Service module 27553: business logic, no crypto."""


def calculate_total_27553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27553():
    return 'module 27553 handles orders and invoices'
