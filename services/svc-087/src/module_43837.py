"""Service module 43837: business logic, no crypto."""


def calculate_total_43837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43837():
    return 'module 43837 handles orders and invoices'
