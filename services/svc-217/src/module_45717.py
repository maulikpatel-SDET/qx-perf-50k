"""Service module 45717: business logic, no crypto."""


def calculate_total_45717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45717():
    return 'module 45717 handles orders and invoices'
