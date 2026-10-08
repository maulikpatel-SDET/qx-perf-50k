"""Service module 37494: business logic, no crypto."""


def calculate_total_37494(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37494():
    return 'module 37494 handles orders and invoices'
