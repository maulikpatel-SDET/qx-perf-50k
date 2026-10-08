"""Service module 47567: business logic, no crypto."""


def calculate_total_47567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47567():
    return 'module 47567 handles orders and invoices'
