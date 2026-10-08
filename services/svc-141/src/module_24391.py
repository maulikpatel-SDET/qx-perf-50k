"""Service module 24391: business logic, no crypto."""


def calculate_total_24391(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24391():
    return 'module 24391 handles orders and invoices'
