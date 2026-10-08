"""Service module 35587: business logic, no crypto."""


def calculate_total_35587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35587():
    return 'module 35587 handles orders and invoices'
