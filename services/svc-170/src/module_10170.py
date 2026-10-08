"""Service module 10170: business logic, no crypto."""


def calculate_total_10170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10170():
    return 'module 10170 handles orders and invoices'
