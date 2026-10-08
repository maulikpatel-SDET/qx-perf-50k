"""Service module 48471: business logic, no crypto."""


def calculate_total_48471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48471():
    return 'module 48471 handles orders and invoices'
