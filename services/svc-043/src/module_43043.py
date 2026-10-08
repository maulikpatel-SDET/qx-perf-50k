"""Service module 43043: business logic, no crypto."""


def calculate_total_43043(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43043():
    return 'module 43043 handles orders and invoices'
