"""Service module 46540: business logic, no crypto."""


def calculate_total_46540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46540():
    return 'module 46540 handles orders and invoices'
