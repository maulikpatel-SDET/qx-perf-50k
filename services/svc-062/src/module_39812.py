"""Service module 39812: business logic, no crypto."""


def calculate_total_39812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39812():
    return 'module 39812 handles orders and invoices'
