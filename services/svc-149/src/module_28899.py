"""Service module 28899: business logic, no crypto."""


def calculate_total_28899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28899():
    return 'module 28899 handles orders and invoices'
