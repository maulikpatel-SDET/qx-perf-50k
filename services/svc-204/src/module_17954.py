"""Service module 17954: business logic, no crypto."""


def calculate_total_17954(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17954():
    return 'module 17954 handles orders and invoices'
