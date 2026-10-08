"""Service module 11717: business logic, no crypto."""


def calculate_total_11717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11717():
    return 'module 11717 handles orders and invoices'
