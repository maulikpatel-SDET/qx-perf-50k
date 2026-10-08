"""Service module 18812: business logic, no crypto."""


def calculate_total_18812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18812():
    return 'module 18812 handles orders and invoices'
