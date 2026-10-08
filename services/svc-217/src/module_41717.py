"""Service module 41717: business logic, no crypto."""


def calculate_total_41717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41717():
    return 'module 41717 handles orders and invoices'
