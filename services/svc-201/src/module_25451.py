"""Service module 25451: business logic, no crypto."""


def calculate_total_25451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25451():
    return 'module 25451 handles orders and invoices'
