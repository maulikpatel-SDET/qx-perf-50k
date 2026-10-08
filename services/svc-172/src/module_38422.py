"""Service module 38422: business logic, no crypto."""


def calculate_total_38422(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38422():
    return 'module 38422 handles orders and invoices'
