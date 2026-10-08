"""Service module 34222: business logic, no crypto."""


def calculate_total_34222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34222():
    return 'module 34222 handles orders and invoices'
