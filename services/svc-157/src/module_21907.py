"""Service module 21907: business logic, no crypto."""


def calculate_total_21907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21907():
    return 'module 21907 handles orders and invoices'
