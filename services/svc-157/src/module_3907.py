"""Service module 3907: business logic, no crypto."""


def calculate_total_3907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3907():
    return 'module 3907 handles orders and invoices'
