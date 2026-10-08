"""Service module 21479: business logic, no crypto."""


def calculate_total_21479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21479():
    return 'module 21479 handles orders and invoices'
