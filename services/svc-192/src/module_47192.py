"""Service module 47192: business logic, no crypto."""


def calculate_total_47192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47192():
    return 'module 47192 handles orders and invoices'
