"""Service module 10479: business logic, no crypto."""


def calculate_total_10479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10479():
    return 'module 10479 handles orders and invoices'
