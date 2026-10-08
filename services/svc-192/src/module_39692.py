"""Service module 39692: business logic, no crypto."""


def calculate_total_39692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39692():
    return 'module 39692 handles orders and invoices'
