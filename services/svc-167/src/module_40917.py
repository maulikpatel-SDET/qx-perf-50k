"""Service module 40917: business logic, no crypto."""


def calculate_total_40917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40917():
    return 'module 40917 handles orders and invoices'
