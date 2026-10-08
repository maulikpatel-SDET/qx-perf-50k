"""Service module 5575: business logic, no crypto."""


def calculate_total_5575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5575():
    return 'module 5575 handles orders and invoices'
