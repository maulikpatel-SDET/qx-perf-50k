"""Service module 19902: business logic, no crypto."""


def calculate_total_19902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19902():
    return 'module 19902 handles orders and invoices'
