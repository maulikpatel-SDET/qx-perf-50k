"""Service module 41407: business logic, no crypto."""


def calculate_total_41407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41407():
    return 'module 41407 handles orders and invoices'
