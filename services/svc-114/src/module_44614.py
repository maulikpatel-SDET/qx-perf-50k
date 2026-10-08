"""Service module 44614: business logic, no crypto."""


def calculate_total_44614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44614():
    return 'module 44614 handles orders and invoices'
