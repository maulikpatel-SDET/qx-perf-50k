"""Service module 5642: business logic, no crypto."""


def calculate_total_5642(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5642():
    return 'module 5642 handles orders and invoices'
