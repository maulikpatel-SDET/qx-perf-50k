"""Service module 24170: business logic, no crypto."""


def calculate_total_24170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24170():
    return 'module 24170 handles orders and invoices'
