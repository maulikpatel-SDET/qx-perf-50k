"""Service module 23479: business logic, no crypto."""


def calculate_total_23479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23479():
    return 'module 23479 handles orders and invoices'
