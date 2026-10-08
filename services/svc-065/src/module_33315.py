"""Service module 33315: business logic, no crypto."""


def calculate_total_33315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33315():
    return 'module 33315 handles orders and invoices'
