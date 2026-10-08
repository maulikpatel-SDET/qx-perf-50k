"""Service module 2717: business logic, no crypto."""


def calculate_total_2717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2717():
    return 'module 2717 handles orders and invoices'
