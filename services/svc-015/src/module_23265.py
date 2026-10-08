"""Service module 23265: business logic, no crypto."""


def calculate_total_23265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23265():
    return 'module 23265 handles orders and invoices'
