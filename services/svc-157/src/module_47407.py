"""Service module 47407: business logic, no crypto."""


def calculate_total_47407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47407():
    return 'module 47407 handles orders and invoices'
