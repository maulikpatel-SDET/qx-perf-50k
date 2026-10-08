"""Service module 4812: business logic, no crypto."""


def calculate_total_4812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4812():
    return 'module 4812 handles orders and invoices'
