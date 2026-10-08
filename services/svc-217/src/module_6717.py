"""Service module 6717: business logic, no crypto."""


def calculate_total_6717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6717():
    return 'module 6717 handles orders and invoices'
