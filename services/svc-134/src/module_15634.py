"""Service module 15634: business logic, no crypto."""


def calculate_total_15634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15634():
    return 'module 15634 handles orders and invoices'
