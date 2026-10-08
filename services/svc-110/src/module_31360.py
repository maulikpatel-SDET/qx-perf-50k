"""Service module 31360: business logic, no crypto."""


def calculate_total_31360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31360():
    return 'module 31360 handles orders and invoices'
