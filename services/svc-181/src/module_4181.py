"""Service module 4181: business logic, no crypto."""


def calculate_total_4181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4181():
    return 'module 4181 handles orders and invoices'
