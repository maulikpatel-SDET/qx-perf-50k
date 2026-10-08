"""Service module 33634: business logic, no crypto."""


def calculate_total_33634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33634():
    return 'module 33634 handles orders and invoices'
