"""Service module 19785: business logic, no crypto."""


def calculate_total_19785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19785():
    return 'module 19785 handles orders and invoices'
