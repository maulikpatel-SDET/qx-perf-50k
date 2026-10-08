"""Service module 16154: business logic, no crypto."""


def calculate_total_16154(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16154():
    return 'module 16154 handles orders and invoices'
