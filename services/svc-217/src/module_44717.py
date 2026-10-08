"""Service module 44717: business logic, no crypto."""


def calculate_total_44717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44717():
    return 'module 44717 handles orders and invoices'
