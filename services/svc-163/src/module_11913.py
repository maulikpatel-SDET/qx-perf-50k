"""Service module 11913: business logic, no crypto."""


def calculate_total_11913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11913():
    return 'module 11913 handles orders and invoices'
