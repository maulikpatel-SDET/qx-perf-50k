"""Service module 34692: business logic, no crypto."""


def calculate_total_34692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34692():
    return 'module 34692 handles orders and invoices'
