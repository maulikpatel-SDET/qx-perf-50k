"""Service module 1992: business logic, no crypto."""


def calculate_total_1992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1992():
    return 'module 1992 handles orders and invoices'
