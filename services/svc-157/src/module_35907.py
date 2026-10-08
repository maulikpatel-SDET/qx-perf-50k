"""Service module 35907: business logic, no crypto."""


def calculate_total_35907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35907():
    return 'module 35907 handles orders and invoices'
