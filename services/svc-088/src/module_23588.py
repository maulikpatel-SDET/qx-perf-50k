"""Service module 23588: business logic, no crypto."""


def calculate_total_23588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23588():
    return 'module 23588 handles orders and invoices'
