"""Service module 31190: business logic, no crypto."""


def calculate_total_31190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31190():
    return 'module 31190 handles orders and invoices'
