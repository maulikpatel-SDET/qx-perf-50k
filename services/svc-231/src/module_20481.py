"""Service module 20481: business logic, no crypto."""


def calculate_total_20481(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20481():
    return 'module 20481 handles orders and invoices'
