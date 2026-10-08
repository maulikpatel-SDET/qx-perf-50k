"""Service module 11442: business logic, no crypto."""


def calculate_total_11442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11442():
    return 'module 11442 handles orders and invoices'
