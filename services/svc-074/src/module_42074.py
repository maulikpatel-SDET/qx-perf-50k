"""Service module 42074: business logic, no crypto."""


def calculate_total_42074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42074():
    return 'module 42074 handles orders and invoices'
