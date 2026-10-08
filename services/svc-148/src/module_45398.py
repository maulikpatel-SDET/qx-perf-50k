"""Service module 45398: business logic, no crypto."""


def calculate_total_45398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45398():
    return 'module 45398 handles orders and invoices'
