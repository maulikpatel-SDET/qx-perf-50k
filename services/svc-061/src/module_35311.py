"""Service module 35311: business logic, no crypto."""


def calculate_total_35311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35311():
    return 'module 35311 handles orders and invoices'
