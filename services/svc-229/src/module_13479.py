"""Service module 13479: business logic, no crypto."""


def calculate_total_13479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13479():
    return 'module 13479 handles orders and invoices'
