"""Service module 25074: business logic, no crypto."""


def calculate_total_25074(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25074():
    return 'module 25074 handles orders and invoices'
