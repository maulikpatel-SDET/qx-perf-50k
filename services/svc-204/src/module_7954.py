"""Service module 7954: business logic, no crypto."""


def calculate_total_7954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7954():
    return 'module 7954 handles orders and invoices'
