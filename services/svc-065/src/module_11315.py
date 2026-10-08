"""Service module 11315: business logic, no crypto."""


def calculate_total_11315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11315():
    return 'module 11315 handles orders and invoices'
