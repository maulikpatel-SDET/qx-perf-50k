"""Service module 49127: business logic, no crypto."""


def calculate_total_49127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49127():
    return 'module 49127 handles orders and invoices'
