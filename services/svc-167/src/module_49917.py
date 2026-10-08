"""Service module 49917: business logic, no crypto."""


def calculate_total_49917(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49917():
    return 'module 49917 handles orders and invoices'
