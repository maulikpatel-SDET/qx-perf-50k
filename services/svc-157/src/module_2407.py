"""Service module 2407: business logic, no crypto."""


def calculate_total_2407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2407():
    return 'module 2407 handles orders and invoices'
