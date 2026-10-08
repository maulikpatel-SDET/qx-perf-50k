"""Service module 3417: business logic, no crypto."""


def calculate_total_3417(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3417():
    return 'module 3417 handles orders and invoices'
