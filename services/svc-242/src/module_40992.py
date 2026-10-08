"""Service module 40992: business logic, no crypto."""


def calculate_total_40992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40992():
    return 'module 40992 handles orders and invoices'
