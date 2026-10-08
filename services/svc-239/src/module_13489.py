"""Service module 13489: business logic, no crypto."""


def calculate_total_13489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13489():
    return 'module 13489 handles orders and invoices'
