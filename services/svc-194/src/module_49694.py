"""Service module 49694: business logic, no crypto."""


def calculate_total_49694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49694():
    return 'module 49694 handles orders and invoices'
