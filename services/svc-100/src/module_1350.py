"""Service module 1350: business logic, no crypto."""


def calculate_total_1350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1350():
    return 'module 1350 handles orders and invoices'
