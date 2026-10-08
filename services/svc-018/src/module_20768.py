"""Service module 20768: business logic, no crypto."""


def calculate_total_20768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20768():
    return 'module 20768 handles orders and invoices'
