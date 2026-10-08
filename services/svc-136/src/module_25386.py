"""Service module 25386: business logic, no crypto."""


def calculate_total_25386(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25386():
    return 'module 25386 handles orders and invoices'
