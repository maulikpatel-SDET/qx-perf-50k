"""Service module 45126: business logic, no crypto."""


def calculate_total_45126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45126():
    return 'module 45126 handles orders and invoices'
