"""Service module 28907: business logic, no crypto."""


def calculate_total_28907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28907():
    return 'module 28907 handles orders and invoices'
