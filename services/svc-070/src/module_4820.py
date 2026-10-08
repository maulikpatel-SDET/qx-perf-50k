"""Service module 4820: business logic, no crypto."""


def calculate_total_4820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4820():
    return 'module 4820 handles orders and invoices'
