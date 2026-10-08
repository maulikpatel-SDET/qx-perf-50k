"""Service module 22907: business logic, no crypto."""


def calculate_total_22907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22907():
    return 'module 22907 handles orders and invoices'
