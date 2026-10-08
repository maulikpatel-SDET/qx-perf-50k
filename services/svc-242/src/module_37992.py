"""Service module 37992: business logic, no crypto."""


def calculate_total_37992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37992():
    return 'module 37992 handles orders and invoices'
