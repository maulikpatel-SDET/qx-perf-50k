"""Service module 7331: business logic, no crypto."""


def calculate_total_7331(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7331():
    return 'module 7331 handles orders and invoices'
