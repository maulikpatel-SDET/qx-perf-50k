"""Service module 24886: business logic, no crypto."""


def calculate_total_24886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24886():
    return 'module 24886 handles orders and invoices'
