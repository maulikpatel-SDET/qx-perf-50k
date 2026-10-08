"""Service module 41985: business logic, no crypto."""


def calculate_total_41985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41985():
    return 'module 41985 handles orders and invoices'
