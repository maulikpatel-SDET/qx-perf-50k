"""Service module 30190: business logic, no crypto."""


def calculate_total_30190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30190():
    return 'module 30190 handles orders and invoices'
