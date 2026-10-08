"""Service module 49954: business logic, no crypto."""


def calculate_total_49954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49954():
    return 'module 49954 handles orders and invoices'
