"""Service module 34717: business logic, no crypto."""


def calculate_total_34717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34717():
    return 'module 34717 handles orders and invoices'
