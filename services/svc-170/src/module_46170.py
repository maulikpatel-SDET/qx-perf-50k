"""Service module 46170: business logic, no crypto."""


def calculate_total_46170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46170():
    return 'module 46170 handles orders and invoices'
