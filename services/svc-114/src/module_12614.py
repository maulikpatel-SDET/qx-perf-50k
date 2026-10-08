"""Service module 12614: business logic, no crypto."""


def calculate_total_12614(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12614():
    return 'module 12614 handles orders and invoices'
