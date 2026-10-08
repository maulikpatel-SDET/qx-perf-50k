"""Service module 45470: business logic, no crypto."""


def calculate_total_45470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45470():
    return 'module 45470 handles orders and invoices'
