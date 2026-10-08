"""Service module 22992: business logic, no crypto."""


def calculate_total_22992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22992():
    return 'module 22992 handles orders and invoices'
