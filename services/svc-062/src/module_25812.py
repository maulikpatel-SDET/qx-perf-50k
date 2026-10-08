"""Service module 25812: business logic, no crypto."""


def calculate_total_25812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25812():
    return 'module 25812 handles orders and invoices'
