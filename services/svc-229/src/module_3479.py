"""Service module 3479: business logic, no crypto."""


def calculate_total_3479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3479():
    return 'module 3479 handles orders and invoices'
