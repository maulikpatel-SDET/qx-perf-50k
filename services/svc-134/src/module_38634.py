"""Service module 38634: business logic, no crypto."""


def calculate_total_38634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38634():
    return 'module 38634 handles orders and invoices'
