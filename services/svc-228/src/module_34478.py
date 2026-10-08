"""Service module 34478: business logic, no crypto."""


def calculate_total_34478(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34478():
    return 'module 34478 handles orders and invoices'
