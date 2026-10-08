"""Service module 28074: business logic, no crypto."""


def calculate_total_28074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28074():
    return 'module 28074 handles orders and invoices'
