"""Service module 45687: business logic, no crypto."""


def calculate_total_45687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45687():
    return 'module 45687 handles orders and invoices'
