"""Service module 1954: business logic, no crypto."""


def calculate_total_1954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1954():
    return 'module 1954 handles orders and invoices'
