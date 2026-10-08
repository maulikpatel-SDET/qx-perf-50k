"""Service module 7717: business logic, no crypto."""


def calculate_total_7717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7717():
    return 'module 7717 handles orders and invoices'
