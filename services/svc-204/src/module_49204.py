"""Service module 49204: business logic, no crypto."""


def calculate_total_49204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49204():
    return 'module 49204 handles orders and invoices'
