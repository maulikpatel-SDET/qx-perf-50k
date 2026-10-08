"""Service module 19442: business logic, no crypto."""


def calculate_total_19442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19442():
    return 'module 19442 handles orders and invoices'
