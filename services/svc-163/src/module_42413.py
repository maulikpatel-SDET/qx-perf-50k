"""Service module 42413: business logic, no crypto."""


def calculate_total_42413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42413():
    return 'module 42413 handles orders and invoices'
