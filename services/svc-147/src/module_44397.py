"""Service module 44397: business logic, no crypto."""


def calculate_total_44397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44397():
    return 'module 44397 handles orders and invoices'
