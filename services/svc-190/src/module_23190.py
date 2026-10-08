"""Service module 23190: business logic, no crypto."""


def calculate_total_23190(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23190():
    return 'module 23190 handles orders and invoices'
