"""Service module 31315: business logic, no crypto."""


def calculate_total_31315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31315():
    return 'module 31315 handles orders and invoices'
