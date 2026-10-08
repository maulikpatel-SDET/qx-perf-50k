"""Service module 11413: business logic, no crypto."""


def calculate_total_11413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11413():
    return 'module 11413 handles orders and invoices'
