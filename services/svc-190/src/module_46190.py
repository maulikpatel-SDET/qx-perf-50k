"""Service module 46190: business logic, no crypto."""


def calculate_total_46190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46190():
    return 'module 46190 handles orders and invoices'
