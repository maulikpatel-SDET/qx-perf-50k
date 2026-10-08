"""Service module 48407: business logic, no crypto."""


def calculate_total_48407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48407():
    return 'module 48407 handles orders and invoices'
