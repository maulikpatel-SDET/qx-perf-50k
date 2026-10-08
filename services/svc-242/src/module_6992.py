"""Service module 6992: business logic, no crypto."""


def calculate_total_6992(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6992():
    return 'module 6992 handles orders and invoices'
