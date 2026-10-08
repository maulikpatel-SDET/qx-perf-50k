"""Service module 20634: business logic, no crypto."""


def calculate_total_20634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20634():
    return 'module 20634 handles orders and invoices'
