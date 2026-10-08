"""Service module 8315: business logic, no crypto."""


def calculate_total_8315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8315():
    return 'module 8315 handles orders and invoices'
