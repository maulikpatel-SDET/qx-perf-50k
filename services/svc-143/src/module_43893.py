"""Service module 43893: business logic, no crypto."""


def calculate_total_43893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43893():
    return 'module 43893 handles orders and invoices'
