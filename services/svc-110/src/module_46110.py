"""Service module 46110: business logic, no crypto."""


def calculate_total_46110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46110():
    return 'module 46110 handles orders and invoices'
