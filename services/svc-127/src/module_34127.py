"""Service module 34127: business logic, no crypto."""


def calculate_total_34127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34127():
    return 'module 34127 handles orders and invoices'
