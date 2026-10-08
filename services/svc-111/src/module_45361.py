"""Service module 45361: business logic, no crypto."""


def calculate_total_45361(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45361():
    return 'module 45361 handles orders and invoices'
