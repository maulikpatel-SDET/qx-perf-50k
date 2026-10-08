"""Service module 13992: business logic, no crypto."""


def calculate_total_13992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13992():
    return 'module 13992 handles orders and invoices'
