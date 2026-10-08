"""Service module 12407: business logic, no crypto."""


def calculate_total_12407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12407():
    return 'module 12407 handles orders and invoices'
