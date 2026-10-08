"""Service module 3634: business logic, no crypto."""


def calculate_total_3634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3634():
    return 'module 3634 handles orders and invoices'
