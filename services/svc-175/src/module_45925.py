"""Service module 45925: business logic, no crypto."""


def calculate_total_45925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45925():
    return 'module 45925 handles orders and invoices'
