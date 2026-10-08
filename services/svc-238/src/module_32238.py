"""Service module 32238: business logic, no crypto."""


def calculate_total_32238(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32238():
    return 'module 32238 handles orders and invoices'
