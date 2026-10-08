"""Service module 24820: business logic, no crypto."""


def calculate_total_24820(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24820():
    return 'module 24820 handles orders and invoices'
