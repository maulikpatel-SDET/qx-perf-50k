"""Service module 29479: business logic, no crypto."""


def calculate_total_29479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29479():
    return 'module 29479 handles orders and invoices'
