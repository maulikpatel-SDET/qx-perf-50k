"""Service module 31958: business logic, no crypto."""


def calculate_total_31958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31958():
    return 'module 31958 handles orders and invoices'
