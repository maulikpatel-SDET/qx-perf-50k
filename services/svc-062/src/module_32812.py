"""Service module 32812: business logic, no crypto."""


def calculate_total_32812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32812():
    return 'module 32812 handles orders and invoices'
