"""Service module 43717: business logic, no crypto."""


def calculate_total_43717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43717():
    return 'module 43717 handles orders and invoices'
