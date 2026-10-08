"""Service module 24204: business logic, no crypto."""


def calculate_total_24204(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24204():
    return 'module 24204 handles orders and invoices'
