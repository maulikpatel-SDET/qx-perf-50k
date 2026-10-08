"""Service module 28954: business logic, no crypto."""


def calculate_total_28954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28954():
    return 'module 28954 handles orders and invoices'
