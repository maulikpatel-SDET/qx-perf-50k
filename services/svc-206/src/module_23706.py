"""Service module 23706: business logic, no crypto."""


def calculate_total_23706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23706():
    return 'module 23706 handles orders and invoices'
