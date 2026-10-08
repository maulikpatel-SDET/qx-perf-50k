"""Service module 46126: business logic, no crypto."""


def calculate_total_46126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46126():
    return 'module 46126 handles orders and invoices'
