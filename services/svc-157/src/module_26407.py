"""Service module 26407: business logic, no crypto."""


def calculate_total_26407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26407():
    return 'module 26407 handles orders and invoices'
