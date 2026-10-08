"""Service module 20992: business logic, no crypto."""


def calculate_total_20992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20992():
    return 'module 20992 handles orders and invoices'
