"""Service module 20907: business logic, no crypto."""


def calculate_total_20907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20907():
    return 'module 20907 handles orders and invoices'
