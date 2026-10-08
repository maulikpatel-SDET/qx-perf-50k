"""Service module 19494: business logic, no crypto."""


def calculate_total_19494(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19494():
    return 'module 19494 handles orders and invoices'
