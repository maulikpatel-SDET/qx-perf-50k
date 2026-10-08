"""Service module 19126: business logic, no crypto."""


def calculate_total_19126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19126():
    return 'module 19126 handles orders and invoices'
