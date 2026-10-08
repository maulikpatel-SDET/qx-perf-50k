"""Service module 43789: business logic, no crypto."""


def calculate_total_43789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43789():
    return 'module 43789 handles orders and invoices'
