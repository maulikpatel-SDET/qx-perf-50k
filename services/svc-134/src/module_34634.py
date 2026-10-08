"""Service module 34634: business logic, no crypto."""


def calculate_total_34634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34634():
    return 'module 34634 handles orders and invoices'
