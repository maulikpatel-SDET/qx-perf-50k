"""Service module 48954: business logic, no crypto."""


def calculate_total_48954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48954():
    return 'module 48954 handles orders and invoices'
