"""Service module 45245: business logic, no crypto."""


def calculate_total_45245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45245():
    return 'module 45245 handles orders and invoices'
