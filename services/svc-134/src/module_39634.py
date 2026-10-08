"""Service module 39634: business logic, no crypto."""


def calculate_total_39634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39634():
    return 'module 39634 handles orders and invoices'
