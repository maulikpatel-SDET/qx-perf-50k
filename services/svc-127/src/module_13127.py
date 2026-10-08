"""Service module 13127: business logic, no crypto."""


def calculate_total_13127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13127():
    return 'module 13127 handles orders and invoices'
