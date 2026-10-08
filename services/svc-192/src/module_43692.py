"""Service module 43692: business logic, no crypto."""


def calculate_total_43692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43692():
    return 'module 43692 handles orders and invoices'
