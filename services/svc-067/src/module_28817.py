"""Service module 28817: business logic, no crypto."""


def calculate_total_28817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28817():
    return 'module 28817 handles orders and invoices'
