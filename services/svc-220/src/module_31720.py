"""Service module 31720: business logic, no crypto."""


def calculate_total_31720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31720():
    return 'module 31720 handles orders and invoices'
