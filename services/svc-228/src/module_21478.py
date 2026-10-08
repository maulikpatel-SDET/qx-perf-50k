"""Service module 21478: business logic, no crypto."""


def calculate_total_21478(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21478():
    return 'module 21478 handles orders and invoices'
