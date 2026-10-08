"""Service module 36717: business logic, no crypto."""


def calculate_total_36717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36717():
    return 'module 36717 handles orders and invoices'
