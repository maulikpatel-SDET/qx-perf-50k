"""Service module 38479: business logic, no crypto."""


def calculate_total_38479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38479():
    return 'module 38479 handles orders and invoices'
