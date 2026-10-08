"""Service module 47843: business logic, no crypto."""


def calculate_total_47843(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47843():
    return 'module 47843 handles orders and invoices'
