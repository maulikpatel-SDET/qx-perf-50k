"""Service module 36985: business logic, no crypto."""


def calculate_total_36985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36985():
    return 'module 36985 handles orders and invoices'
