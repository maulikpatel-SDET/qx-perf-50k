"""Service module 18190: business logic, no crypto."""


def calculate_total_18190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18190():
    return 'module 18190 handles orders and invoices'
