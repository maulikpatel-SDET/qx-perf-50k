"""Service module 44992: business logic, no crypto."""


def calculate_total_44992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44992():
    return 'module 44992 handles orders and invoices'
