"""Service module 41160: business logic, no crypto."""


def calculate_total_41160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41160():
    return 'module 41160 handles orders and invoices'
