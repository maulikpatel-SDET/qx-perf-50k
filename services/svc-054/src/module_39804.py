"""Service module 39804: business logic, no crypto."""


def calculate_total_39804(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39804():
    return 'module 39804 handles orders and invoices'
