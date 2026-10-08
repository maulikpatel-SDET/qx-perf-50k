"""Service module 41473: business logic, no crypto."""


def calculate_total_41473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41473():
    return 'module 41473 handles orders and invoices'
