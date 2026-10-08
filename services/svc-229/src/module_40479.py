"""Service module 40479: business logic, no crypto."""


def calculate_total_40479(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40479():
    return 'module 40479 handles orders and invoices'
