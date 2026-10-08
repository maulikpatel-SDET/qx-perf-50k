"""Service module 23160: business logic, no crypto."""


def calculate_total_23160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23160():
    return 'module 23160 handles orders and invoices'
